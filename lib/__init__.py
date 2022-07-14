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

network_node_0 = NetworkNode(node_ip="200.232.166.142", wallet_node=Wallet())

print("\n", repr(network_node_0))


print("\n\n", "MINING A BLOCK:  ...")

obtained_nonce = NetworkNode.mine_block(nonce_leading_zeros=1)

print("\nObtained nonce hash: " + hashlib.sha256(obtained_nonce.encode("utf-8")).hexdigest())