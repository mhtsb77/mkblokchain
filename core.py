import hashlib
import json
from datetime import datetime


# ==========================================
# CLASS BLOCK
# ==========================================

class Block:

    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + json.dumps(self.data, sort_keys=True, default=str)
            + str(self.previous_hash)
        )

        return hashlib.sha256(
            block_string.encode()
        ).hexdigest()


# ==========================================
# CLASS BLOCKCHAIN
# ==========================================

class Blockchain:

    def __init__(self):
        self.chain = []

        # Buat blok pertama
        self.create_genesis_block()

    # ======================================
    # GENESIS BLOCK
    # ======================================

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            data={
                "type": "Genesis Block",
                "message": "Blockchain Supply Chain"
            },
            previous_hash="0"
        )

        self.chain.append(genesis_block)

    # ======================================
    # GET BLOCK TERAKHIR
    # ======================================

    def get_latest_block(self):
        return self.chain[-1]

    # ======================================
    # ADD BLOCK
    # ======================================

    def add_block(self, data):
        previous_block = self.get_latest_block()

        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=previous_block.hash
        )

        self.chain.append(new_block)

        return new_block

    # ======================================
    # VALIDASI BLOCKCHAIN
    # ======================================

    def is_chain_valid(self):

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Cek hash block
            if current_block.hash != current_block.calculate_hash():
                return False

            # Cek hubungan previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True
import json
from datetime import datetime


# ==========================================
# CLASS BLOCK
# ==========================================

class Block:

    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + json.dumps(self.data, sort_keys=True, default=str)
            + str(self.previous_hash)
        )

        return hashlib.sha256(
            block_string.encode()
        ).hexdigest()


# ==========================================
# CLASS BLOCKCHAIN
# ==========================================

class Blockchain:

    def __init__(self):
        self.chain = []

        # Buat blok pertama
        self.create_genesis_block()

    # ======================================
    # GENESIS BLOCK
    # ======================================

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            data={
                "type": "Genesis Block",
                "message": "Blockchain Supply Chain"
            },
            previous_hash="0"
        )

        self.chain.append(genesis_block)

    # ======================================
    # GET BLOCK TERAKHIR
    # ======================================

    def get_latest_block(self):
        return self.chain[-1]

    # ======================================
    # ADD BLOCK
    # ======================================

    def add_block(self, data):
        previous_block = self.get_latest_block()

        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=previous_block.hash
        )

        self.chain.append(new_block)

        return new_block

    # ======================================
    # VALIDASI BLOCKCHAIN
    # ======================================

    def is_chain_valid(self):

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Cek hash block
            if current_block.hash != current_block.calculate_hash():
                return False

            # Cek hubungan previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True