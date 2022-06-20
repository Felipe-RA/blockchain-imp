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
        self.hashed_value = hashlib.sha256(input_value.encode("utf-8")).hexdigest()

    def __repr__(self) -> str:
        return "left leave: " + str(self.left_leave) + "right leave: " + str(self.right_leave) \
             + "Hash: " + str(self.hashed_value)

    def __str__(self) -> str:
        return str(self.left_leave) + str(self.right_leave) +  str(self.hashed_value)


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