# Blockchain Imp

A crude implementation of the `Bitcoin System` proposed by Satoshi; using Python.

You can find the original WhitePaper here: [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)

---

## Instructions

"Please run the __init__.py module to run a test of the libs"

## Guidelines


- All classes and functions are documented, do take a look in case you do not understand any implementation logic.
- `Wallet()` to create a SHA256 generated wallet. It will ask you to put some gibberish to increase entropy, but this is not required.
- `Transaction(wallet,inputs,outputs)` to create a new transaction. 
- `NetworkNode(node_ip, wallet_node)` to create a new Node on the BlockChain Network (this is just for semantic consistency purposes, there are no real Network capabilities implemented at this moment)
- This `~NetworkNode` object will be the one that will search for a nonce, will verify Transactions and will generate a new block.
- This `~NetworkNode` object will be the one responsible for creating as Merkle Tree using the `~HashedNode` object and the `create_tree()` functions
- Finally, the `~NetworkNode` creates a new `~Block` object. The creation of this `~Block` will be different if its defined as `is_genesis = True` on creation. In this case we will use the default value '0' as previous hash for the creation of the `Genesis ~Block`

All Objects implemented within this repository have a specialized `str()` implementation to facilitate the hashing of the objects. Feel free to print some objects as a string!