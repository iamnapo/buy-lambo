# buy-lambo

> Scripts to create a BTC address whose assets are locked until a specified time (or block) and after that time, transfer all funds to another address.

[![Travis](https://img.shields.io/travis/com/iamnapo/buy-lambo.svg?style=flat-square&logo=travis&label=)](https://travis-ci.com/iamnapo/buy-lambo) [![license](https://img.shields.io/github/license/iamnapo/buy-lambo.svg?style=flat-square)](./LICENSE)

## Install

* Install (and run) [Bitcoin Core](https://bitcoin.org/en/bitcoin-core/)
* Install [Python 3](https://www.python.org/downloads/)
* Run `pip3 install -r requirements.txt`
* Configure `.env.sample` and rename it to `.env`

## Usage

```bash
$ python3 create_HODL_address.py --help
$ python3 buy_lambo.py --help
```

## Example

```bash
$ python3 create_HODL_address.py --priv_key cNxmxYnXjdH8j1JwumuSF5HtLpjSDHv7x4ZWUQSf16mF4RxaYFnt --lock 1735689600
Time-locked address: 2MstzXj1jLkqnBgyaJFWmwkKSL9RsEv3XaE
```

Send BTCs to that address through the years...

At 01/01/2025:

```bash
$ python3 buy_lambo.py --priv_key cNxmxYnXjdH8j1JwumuSF5HtLpjSDHv7x4ZWUQSf16mF4RxaYFnt --lock 1735689600 --from_addr 2MstzXj1jLkqnBgyaJFWmwkKSL9RsEv3XaE --to_addr mmadWC5qCn2JHr6mC3v4vba35wa71xATGb
Sent to Block-chain!
```

[Buy Lamborghini](https://www.lamborghini.com/en-en/ownership/dealer-locator)

## License

MIT © [Napoleon-Christos Oikonomou](https://iamnapo.me)
