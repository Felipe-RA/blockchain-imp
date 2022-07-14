import hashlib
import random
import string

class Wallet:

    """
    A Wallet generator using pseudo random numbers, some entropy from the user and SHA256 hashing
    No parameters needed.
    """

    def __init__(self) -> None:


        gibberish = input("Insert Gibberish to increase entropy!: ")
        pub_key_seed = ''.join(random.choice(string.ascii_letters + string.digits + str(gibberish)) for i in range(64))
        priv_key_seed = ''.join(random.choice(string.ascii_letters + string.digits + str(gibberish[::-1])) for i in range(64))

        self.public_key = hashlib.sha256(pub_key_seed.encode("utf-8")).hexdigest()
        priv_key = hashlib.sha256(priv_key_seed.encode("utf-8")).hexdigest()
        print("\nPrivate Key: YOU MUST WRITE IT DOWN IT WILL NOT BE STORED: ", priv_key)

        signature_str = self.public_key + priv_key
        self.signature =  hashlib.sha256(signature_str.encode("utf-8")).hexdigest()
        self.balance = 0


    def __str__(self) -> str:
        return "Public key: " + self.public_key + " Signature: " + self.signature + " Balance: " + str(self.balance)

    
