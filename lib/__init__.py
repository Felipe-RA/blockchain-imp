from Transaction import *
from Block import *
from HashedNode import *
from NetworkNode import *
from Wallet import *

from utils import *
import hashlib

print("\nFIRST WALLET:\n")
wallet_0 = Wallet()
print("\nWallet Info: ",wallet_0)

print("\nSECOND WALLET:\n")
wallet_1 = Wallet()
print("\nWallet Info: ",wallet_1)

tx_0 = Transaction(
        wallet_0,
        inputs=[3],
        outputs=[
            (2.7, wallet_1.public_key),
            (0.3, wallet_0.public_key)
        ],
        genesis=True
    )

print("\n\n",repr(tx_0))


print("\n\n", "CREATION OF NETWORK NODE\n")

print("\nSince it's a new node, we will create a wallet for the node: ")
network_node_0 = NetworkNode(node_ip="200.232.166.142", wallet_node=Wallet())

print("\n", repr(network_node_0))


print("\n\n", "MINING A BLOCK:  ...")

obtained_nonce = NetworkNode.mine_block()

print("\nObtained nonce hash: " + hashlib.sha256(obtained_nonce.encode("utf-8")).hexdigest())
print("Obtained nonce: " + obtained_nonce)

print("\n\n", "CREATION OF BLOCK AND ADDING PREV. TRANSACTION\n")

block_0 = network_node_0.create_block([tx_0], awarded_coins=50, is_genesis_block=True)

print("\n",repr(block_0))