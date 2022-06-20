import hashlib

class HashedNode:
    """
    An implementation of a Merkle Node using sha256 hashing.
    Values are utf-8 forced before hashing.
    
    Attributes are self explanatory
    """
    def __init__(self, input_value) -> object:
        self.left_leave = None
        self.right_leave = None
        self.input_value = input_value
        self.hashed_value = hashlib.sha256(input_value.encode("utf-8")).hexdigest()

    def __repr__(self) -> str:
        return "left leave: " + str(self.left_leave) + "right leave: " + str(self.right_leave) \
             + "Hash: " + str(self.hashed_value) + "Input Value:" + self.input_value

    def __str__(self) -> str:
        return str(self.left_leave) + str(self.right_leave) + str(self.input_value) + str(self.hashed_value) 

class Transaction:
    """
    A transaction between two parties, user0 and user1
    """
    
    def __init__(self, user_1_public_key: str, inputs = [], outputs = [], prev_transaction_hash = '0' ,genesis = False) -> object:

        """
        Constructor for a transaction.
        
        Params:
        user_1_public_key: A string with the provided public key from the user0
        inputs: A list with the coins that are entering the transaction
        outputs: A list with the coins that are exiting the transaction (for multiple outputs, and change if any)
        prev_transaction_hash: A string with the hashed value of the previous transaction. Default is '0' for the first transaction ever.
        genesis: A boolean flag to mark if a transaction is the first one
        """

        self.user_1_public_key = user_1_public_key
        self.inputs = inputs
        self.outputs = outputs
        self.prev_transaction_hash = prev_transaction_hash

        if genesis:
            user_0_signature = '0'
            concat_string = str(self.user_1_public_key) + str(prev_transaction_hash)
            concat_string = hashlib.sha256(concat_string.encode("utf-8")).hexdigest() + user_0_signature

            self.user_0_signature = hashlib.sha256(concat_string.encode("utf-8")).hexdigest()
        else:
            concat_string = str(self.user_1_public_key) + str(prev_transaction_hash)
            concat_string = hashlib.sha256(concat_string.encode("utf-8")).hexdigest() + input("Input your Private Key: ")

            self.user_0_signature = hashlib.sha256(concat_string.encode("utf-8")).hexdigest()

    def __repr__(self) -> str:
        return "Transaction with: " + "User1PublicKey: " + str(self.user_1_public_key) + \
            "TransactionInputs: " + str(self.inputs) + "TransactionOutputs: " + str(self.outputs) + \
            "HashPreviousTransaction:" + str(self.prev_transaction_hash)

    def __str__(self) -> str:
        return str(self.user_1_public_key) + str(self.inputs) + str(self.outputs) + str(self.prev_transaction_hash)

class MetadataBlockchain:
    used_nonces = []
    def __init__(self) -> None:
        pass
    
    @classmethod
    def is_valid_nonce(nonce_to_check):
        if nonce_to_check[0:4] != "0000":
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

    def __init__(self, merkle_root: HashedNode, nonce: str, previous_block = '0', is_genesis_block = False, transactions_per_block = 4) -> object:
        """
        previous_block_hash will initialize as a '0'  for the first instance of the program
        is_genesis_block: a boolean flag to indicate the first object
        transactions_pero_block: an integer with the predefined number of transactions.

        we check that the nonce is correct by applying sha256 and checking the number of leading zeros
        """ 

        ## sanity checks
        if previous_block == '0' and is_genesis_block == False:
            raise ValueError("Detected incorrect input for previous block on non genesis block")

        nonce_to_check = hashlib.sha256(nonce.encode("utf-8")).hexdigest()

        if not MetadataBlockchain.is_valid_nonce(nonce_to_check):
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

        