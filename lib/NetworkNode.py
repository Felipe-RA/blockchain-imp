from Block import *
from utils import *
import string
import hashlib
from random import choice

class NetworkNode:
    """
    A basic simulation of a Node from a BlockChain Network.
    It basically just mines and collects transactions.

    No competition with other nodes implemented
    """
    def __init__(self, node_ip: string, wallet_node: Wallet) -> None:
        self.wallet_node = wallet_node
        self.node_ip = node_ip

    @classmethod
    def mine_block(self, nonce_leading_zeros = 4) -> str:
        """
        Mines a block, just increments a string using ascii letters and hexdigits,
        applies sha256 and evaluates if it has the required
        number of leading zeros

        params:
        nonce_leading_zeros: number of zeros that the searched nonce must have at the start. default 4

        returns:
        a string containing the required nonce

        """

        #string_space = string.ascii_letters+string.hexdigits
        string_space = string.ascii_letters+string.hexdigits
        searching_nonce = ""
        flag = True

        while flag:
            for i in string_space:
                searching_nonce = "".join(choice(string_space) for i in range(64))
                if hashlib.sha256(searching_nonce.encode("utf-8")).hexdigest()[0:nonce_leading_zeros] == "0"*nonce_leading_zeros:
                    flag =  False
                    break

        return searching_nonce

    def create_block(self, list_of_transactions:list , awarded_coins = 50.0, is_genesis_block = False) -> Block:
        """
        A function that receives transactions, checks their validity and creates a new block
        FIRST TRANSACTION IS ALWAYS THE REWARD FOR THE NETWORK NODE

        params:
        list of transactions: list with ~Transaction Objects
        is_genesis_block: Boolean to indicate if a Block is the first one of the Chain.
        awarded_coins: Number of awarded coins. a float
        
        returns:
        a ~Block object
        """


        if is_genesis_block:

            ## we INSERT a transaction at the start of the list of transactions with the miners commission
            list_of_transactions.insert(0,
                                Transaction(self.wallet_node,
                                            inputs = [awarded_coins],
                                            outputs=[(self.wallet_node.public_key, awarded_coins)],
                                            genesis=True
                                            )
                                        )
            merkle_root = create_tree([str(i) for i in list_of_transactions])
            nonce = NetworkNode.mine_block()

            return Block(merkle_root,nonce, is_genesis_block = True)

        else:
            ## we INSERT a transaction at the start of the list of transactions with the miners commission
            list_of_transactions.insert(0,
                                Transaction(self.wallet_node,
                                            inputs = [awarded_coins],
                                            outputs=[(self.wallet_node.public_key, awarded_coins)],
                                            )
                                        )

            merkle_root = create_tree([str(i) for i in list_of_transactions])
            nonce = NetworkNode.mine_block()

            return Block(merkle_root, nonce)


    def __repr__(self) -> str:
        
        return "Node IP:" + self.node_ip + "\nNode Wallet Public Key: " + self.wallet_node.public_key




