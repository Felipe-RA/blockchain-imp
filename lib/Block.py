import hashlib
from HashedNode import *
from Transaction import *


class MetadataBlockchain:
    used_nonces = []
    def __init__(self) -> None:
        pass
    
    @classmethod
    def is_valid_nonce(self, nonce_to_check):
        if nonce_to_check[0:3] != "000":
            return False
        if nonce_to_check in MetadataBlockchain.used_nonces:
            return False
        return True

class Block:
    """
    A Block that contains all the information required to assert proof of work.

    Contrary to the suggestion of Satoshi, the difficulty of our Nonce will be fixed to 4 leading zeros
    instead of using a moving average. This is for the sake of simplicity.
    """

    def __init__(self, merkle_root: HashedNode, nonce: str, previous_block = '0',
                 is_genesis_block = False, transactions_per_block = 4
                ) -> None:
        """
        previous_block_hash will initialize as a '0'  for the first instance of the program
        is_genesis_block: a boolean flag to indicate the first object
        transactions_pero_block: an integer with the predefined number of transactions.

        we check that the nonce is correct by applying sha256 and checking the number of leading zeros
        """ 

        ## sanity checks
        if previous_block == '0' and is_genesis_block == False:
            raise ValueError("Detected incorrect input for previous block on non genesis block")

        
        check_nonce = hashlib.sha256(nonce.encode("utf-8")).hexdigest()
        print("DEBUG",check_nonce,type(check_nonce) )

        if not MetadataBlockchain.is_valid_nonce(check_nonce):
            raise ValueError("Nonce is not correct!")
        ## end sanity checks


        self.merkle_root = merkle_root
        self.nonce = nonce

        if is_genesis_block:
            self.previous_block_hash = previous_block
        else:
            self.previous_block_hash = hashlib.sha256(str(previous_block).encode("utf-8")).hexdigest()


    def __repr__(self) -> str:
        return "Block Info: " + "\nPrevious Block Hash:\n" + self.previous_block_hash + \
            "\nMerkle Root Hash:\n" + self.merkle_root.hashed_value + \
            "\nNonce: " + self.nonce

    def __str__(self) -> str:
        return self.previous_block_hash + self.merkle_root.hashed_value + self.nonce

