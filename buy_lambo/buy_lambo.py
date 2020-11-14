import os
from decimal import Decimal

import requests
from bitcoinutils.constants import SATOSHIS_PER_BITCOIN, TYPE_ABSOLUTE_TIMELOCK
from bitcoinutils.keys import P2pkhAddress, PrivateKey
from bitcoinutils.proxy import NodeProxy
from bitcoinutils.script import Script
from bitcoinutils.setup import setup
from bitcoinutils.transactions import Locktime, Sequence, Transaction, TxInput, TxOutput
from dotenv import load_dotenv

load_dotenv()


def buy_lambo(key, lock, from_addr, to_addr):
    setup(os.getenv("BUY_LAMBO_BTC_NET", "regtest"))

    # Create a proxy to JSON-RPC api
    chain = NodeProxy(os.getenv("BUY_LAMBO_RPC_USER", "rpcuser"), os.getenv("BUY_LAMBO_RPC_PASSWORD", "rpcpassword")).get_proxy()

    # Try executing a command to see if node is running
    try:
        chain.getblockcount()
    except Exception:
        print("Error: Node isn't working!")
        return

    # Check addresses
    if not chain.validateaddress(from_addr)["isvalid"]:
        print("Error: `from_addr` is not a valid address!")
        return
    if not chain.validateaddress(to_addr)["isvalid"]:
        print("Error: `to_addr` is not a valid address!")
        return

    # Set lock sequence prefix
    seq = Sequence(TYPE_ABSOLUTE_TIMELOCK, lock)

    # Get public key (found from private key)
    private_key = PrivateKey(key)
    public_key = private_key.get_public_key()

    # Add address to wallet so we can get utxos from bitcoin core
    chain.importaddress(from_addr)

    # Get UTXOs
    utxos = chain.listunspent(1, 9999999, [from_addr])

    # Create inputs
    txin = []
    total_btc = Decimal(0)
    for utxo in utxos:
        # Note that for each input we set the correct nSequence
        txin.append(TxInput(utxo["txid"], utxo["vout"], sequence=seq.for_input_sequence()))
        total_btc = total_btc + utxo["amount"]

    if total_btc == 0:
        return print("\nThere aren't any UTXOs :(.")

    # Create a fee-less output
    txout = TxOutput(total_btc - Decimal(0.1), P2pkhAddress(to_addr).to_script_pub_key())

    # Create dummy transaction (to calculate size)
    tx = Transaction([TxInput.copy(inpt) for inpt in txin], [txout], locktime=Locktime(lock).for_transaction())

    # create the redeem script - needed to sign the transaction
    redeem_script = Script(
        [
            seq.for_script(),
            "OP_CHECKLOCKTIMEVERIFY",
            "OP_DROP",
            "OP_DUP",
            "OP_HASH160",
            public_key.get_address().to_hash160(),
            "OP_EQUALVERIFY",
            "OP_CHECKSIG",
        ]
    )

    # use the private key corresponding to the address that contains the
    # UTXO we are trying to spend to create the signature for the txin -
    # note that the redeem script is passed to replace the scriptSig
    for ind, txinput in enumerate(tx.inputs):
        sig = private_key.sign_input(tx, ind, redeem_script)
        txinput.script_sig = Script([sig, public_key.to_hex(), redeem_script.to_hex()])

    # Calculate fees
    sat_per_byte = requests.get("https://bitcoinfees.earn.com/api/v1/fees/recommended").json()["fastestFee"]
    fee = Decimal(max((len(bytes.fromhex(tx.serialize())) * sat_per_byte) / SATOSHIS_PER_BITCOIN, 0))
    if fee == 0:
        print("WARNING: There isn't enough balance to calculate fees.")

    # Create final tx with correct txout value
    txout = TxOutput(total_btc - fee, P2pkhAddress(to_addr).to_script_pub_key())
    tx = Transaction([TxInput.copy(inpt) for inpt in tx.inputs], [txout], locktime=Locktime(lock).for_transaction())
    for ind, txinput in enumerate(tx.inputs):
        sig = private_key.sign_input(tx, ind, redeem_script)
        txinput.script_sig = Script([sig, public_key.to_hex(), redeem_script.to_hex()])
    signed_tx = tx.serialize()

    # print raw transaction
    print("\nRaw unsigned transaction:\n{}".format(Transaction(txin, [txout]).serialize()))

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n{}".format(signed_tx))
    print("\nTxId: {}".format(tx.get_txid()))

    # Check if is valid and send it
    if chain.testmempoolaccept([signed_tx])[0]["allowed"]:
        chain.sendrawtransaction(signed_tx)
        print("\nSent to Block-chain! Have fun with those {} BTC.".format(total_btc - fee))
    else:
        print("\nCan't send (yet)!")
        print("Reason: `{}`".format(chain.testmempoolaccept([signed_tx])[0]["reject-reason"]))
