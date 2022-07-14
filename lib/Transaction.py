import hashlib
from Wallet import *

class Transaction:
    """
    A transaction between two parties, user0 and user1
    """
    
    def __init__(self, user_1_wallet: Wallet, inputs = [], outputs = [], prev_transaction_hash = '0' ,genesis = False) -> None:

        """
        Constructor for a transaction.
        
        Params:
        user_1_wallet: A ~Wallet object from the user that starts a transaction
        inputs: A list with the coins that are entering the transaction

        outputs: A list with tuples: coins that are exiting the transaction
            (for multiple outputs, and change if any), and the respective public keys of the wallets

        prev_transaction_hash: A string with the hashed value of the previous transaction.
            Default is '0' for the first transaction ever.

        genesis: A boolean flag to mark if a transaction is the first one
        """

        self.user_1_public_key = user_1_wallet.public_key
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
        return "TRANSACTION INFO:\n" + "User1PublicKey: " + str(self.user_1_public_key) + \
            "\nTransactionInputs: " + str(self.inputs) + "\nTransactionOutputs: " + str(self.outputs) + \
            "\nHashPreviousTransaction:" + str(self.prev_transaction_hash)

    def __str__(self) -> str:
        return str(self.user_1_public_key) + str(self.inputs) + str(self.outputs) + str(self.prev_transaction_hash)