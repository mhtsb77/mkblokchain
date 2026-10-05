import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash, timestamp=None):
        self.index = index
        self.timestamp = timestamp if timestamp else time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )

        return hashlib.sha256(
            block_string.encode()
        ).hexdigest()


class Blockchain:
    def __init__(self):
        # Menyimpan semua block
        self.chain = []

        # Membuat block pertama / genesis block
        self.create_genesis_block()

    # ==========================================
    # GENESIS BLOCK
    # ==========================================
    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            data="Genesis Block - Toko Stone Island",
            previous_hash="0"
        )

        self.chain.append(genesis_block)

    # ==========================================
    # MENDAPATKAN BLOCK TERAKHIR
    # ==========================================
    def get_latest_block(self):
        return self.chain[-1]

    # ==========================================
    # MENAMBAHKAN BLOCK BARU
    # ==========================================
    def add_block(self, data):
        latest_block = self.get_latest_block()

        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=latest_block.hash
        )

        self.chain.append(new_block)

    # ==========================================
    # VALIDASI BLOCKCHAIN
    # ==========================================
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Cek hash block
            if current_block.hash != current_block.calculate_hash():
                return False

            # Cek hubungan dengan block sebelumnya
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    # ==========================================
    # MENGAMBIL SEMUA BLOCK
    # ==========================================
    def get_all_blocks(self):
        return self.chain

    # ==========================================
    # JUMLAH BLOCK
    # ==========================================
    def get_block_count(self):
        return len(self.chain)