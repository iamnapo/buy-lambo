import os

from bitcoinutils.constants import TYPE_ABSOLUTE_TIMELOCK
from bitcoinutils.keys import P2shAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script
from bitcoinutils.setup import setup
from bitcoinutils.transactions import Sequence
from dotenv import load_dotenv

load_dotenv()


def create_HODL_address(key, lock, is_priv=False):
    setup(os.getenv("BUY_LAMBO_BTC_NET", "regtest"))

    # Get public key (given or found from private key)
    public_key = PrivateKey(key).get_public_key() if is_priv else PublicKey(key)

    # Get address from public key
    address_from_key = public_key.get_address()

    # Set lock sequence prefix
    seq = Sequence(TYPE_ABSOLUTE_TIMELOCK, lock)

    # create the redeem script - needed to sign the transaction
    redeem_script = Script(
        [
            seq.for_script(),
            "OP_CHECKLOCKTIMEVERIFY",
            "OP_DROP",
            "OP_DUP",
            "OP_HASH160",
            address_from_key.to_hash160(),
            "OP_EQUALVERIFY",
            "OP_CHECKSIG",
        ]
    )

    # create a P2SH address from a redeem script
    addr = P2shAddress.from_script(redeem_script)
    print("Time-locked address: {}".format(addr.to_string()))
