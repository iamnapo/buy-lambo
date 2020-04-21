import os
from argparse import ArgumentParser

from bitcoinutils.constants import TYPE_ABSOLUTE_TIMELOCK
from bitcoinutils.keys import P2shAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script
from bitcoinutils.setup import setup
from bitcoinutils.transactions import Sequence
from dotenv import load_dotenv

load_dotenv()


def main(key, lock, is_priv=False):
    setup(os.getenv("BTC_NET", "regtest"))

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
    print("Time-locked address: {}".format(addr.to_address()))


if __name__ == "__main__":
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--pub_key", dest="pub_key", default=None, type=str, help="Public key to use."
    )
    group.add_argument(
        "--priv_key",
        dest="priv_key",
        default=None,
        type=str,
        help="Private key to use.",
    )
    parser.add_argument(
        "--lock",
        dest="lock",
        required=True,
        type=int,
        help="Time used to lock the address. If <500 million is treated as block height, else as UNIX time.",
    )
    args = parser.parse_args()

    main(key=args.priv_key, lock=args.lock, is_priv=args.priv_key)
