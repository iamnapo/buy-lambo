# buy-lambo

> Scripts to create a BTC address whose assets are locked until a specified time (or block) and after that time, transfer all funds to another address.

[![build](https://img.shields.io/github/workflow/status/iamnapo/buy-lambo/Install%20%26%20test?style=for-the-badge&logo=github&label=)](https://github.com/iamnapo/buy-lambo/actions) [![license](https://img.shields.io/github/license/iamnapo/buy-lambo.svg?style=for-the-badge)](./LICENSE)

## Install

- Install (and run) [Bitcoin Core](https://bitcoin.org/en/bitcoin-core/)
- Install [Python 3](https://www.python.org/downloads/)
- Run `pip3 install -r requirements.txt`
- Configure `.env.sample` and rename it to `.env`

## Usage

```sh
$ python3 buy_lambo/create_HODL_address.py --help
$ python3 buy_lambo/buy_lambo.py --help
```

## Example

```sh
$ python3 buy_lambo/create_HODL_address.py --priv_key cNxmxYnXjdH8j1JwumuSF5HtLpjSDHv7x4ZWUQSf16mF4RxaYFnt --lock 1735689600
Time-locked address: 2MstzXj1jLkqnBgyaJFWmwkKSL9RsEv3XaE
```

Send BTCs to that address through the years...

At 01/01/2025:

```sh
$ python3 buy_lambo/buy_lambo.py --priv_key cNxmxYnXjdH8j1JwumuSF5HtLpjSDHv7x4ZWUQSf16mF4RxaYFnt --lock 1735689600 --from_addr 2MstzXj1jLkqnBgyaJFWmwkKSL9RsEv3XaE --to_addr mmadWC5qCn2JHr6mC3v4vba35wa71xATGb
Raw unsigned transaction:
02000000031ea3eebed927cd62c43f693232bd921890289a104cff95730bc036cdf5fc62720000000000feffffff7713218148c956ed72a9c2748d516ef97a583812897928325c88526aff2f45bf0100000000feffffff865e9116b42b6969c73a98769a55fe16295d0199556b3f5834d2b0e338d131c80100000000feffffff01c03a0cae040000001976a9144282bb9b8202cfd5fb04eafc91a87018bed4a53488ac00000000

Raw signed transaction:
02000000031ea3eebed927cd62c43f693232bd921890289a104cff95730bc036cdf5fc6272000000008c483045022100bb439cafcb8baeca5c933e860450c14718b946e4560e22f85a3e38ac5c46051c02201eb8587953b1e72e8676e9e60c795c1c07a64ee9d86f2890053dd27dba2a709201210270b33524406a8c11def57e11994b4d93c36c31822a454172e0018cb3804c96e1200480857467b17576a9144282bb9b8202cfd5fb04eafc91a87018bed4a53488acfeffffff7713218148c956ed72a9c2748d516ef97a583812897928325c88526aff2f45bf010000008c4830450221009b9e4a3a4ecff2009dacb42463af27e63ff1c9f3cfe6f60607490280fbc62dd20220522182480822444bd8455b774e611f308325079af320c2d834338ffa755b5acd01210270b33524406a8c11def57e11994b4d93c36c31822a454172e0018cb3804c96e1200480857467b17576a9144282bb9b8202cfd5fb04eafc91a87018bed4a53488acfeffffff865e9116b42b6969c73a98769a55fe16295d0199556b3f5834d2b0e338d131c8010000008b4730440220498ddc0e30e98fc02276a21b90d14d84a48a21c8a9da126320518a2ad5071cb002201f15eeec6ffe3d2e02222e99add3213f398600e1f53c276b61b67d2f70b8eeb301210270b33524406a8c11def57e11994b4d93c36c31822a454172e0018cb3804c96e1200480857467b17576a9144282bb9b8202cfd5fb04eafc91a87018bed4a53488acfeffffff01c03a0cae040000001976a9144282bb9b8202cfd5fb04eafc91a87018bed4a53488ac80857467

TxId: b22a0ed64755128148029d73f8bfc80f99ac492152ab1b9cc7e5fabf14c214e6

Sent to Block-chain! Have fun with those 200.99906240 BTC.
```

[Buy Lamborghini](https://www.lamborghini.com/en-en/ownership/dealer-locator)
