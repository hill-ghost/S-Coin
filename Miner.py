import time
import json
import random
import hashlib

from Block import Block

class Miner(object):
    def mine(self, index, previous_hash, transaction_data):
        begin_time = time.time()

        block = Block()
        block.index = index
        block.previous_hash = previous_hash
        block.transaction_data = transaction_data
        block.timestamp = time.time()

        block.difficulty, block.hash, block.nonce = self.gen_hash(previous_hash, transaction_data)
        end_time = time.time()
        spend_time = end_time - begin_time

        return block, spend_time

    def gen_hash(previous_hash, transaction_data):
        nonce = random.randrange(1, 99999)

        difficulty = 0

        guess = str(previous_hash) + str(nonce) + transaction_data

        res = hashlib.sha256(guess.encode()).hexdigest()

        while res[-1] != '0':
            difficulty += 1
            nonce += difficulty
            guess = previous_hash + str(nonce) + transaction_data
            res = hashlib.sha256(guess.encode()).hexdigest()

        return difficulty, res, nonce
            
