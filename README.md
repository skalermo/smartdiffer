# smartdiffer
Tool to compare smart contracts source code.

Heavily relies on API of [Etherscan](https://etherscan.io/) and [Diffchecker](https://www.diffchecker.com).

## Installation

```sh
pip install smartdiffer
```

## Usage

Provide two sources you wish to compare. *Source* is either `address` of a smart contract on ethereum mainnet or `path` to a local file.

```sh
smartdiffer 0x0123456789abcdef0123456789abcdef01234567 path/to/local/file
```

On the completion you'll get a link to the diff on [diffchecker.com](https://www.diffchecker.com).



