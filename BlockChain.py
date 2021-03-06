import json
import random
import string
import hashlib
import time

from Miner import Miner
from Block import Block
from MyThread import MyThread

from threading import Thread
from decimal import Decimal

class BlockChain(object):
    def __init__(self, hash_num):
        self.chain_list = []

        self.miner_list = []

        for i in range(6):
            self.miner_list.append(Miner)

            self.result_list = []

            self.gen_block(hash_num)

    @property
    def get_last_block(self):
        if len(self.chain_list):
            return self.chain_list[-1]
        return None

    def get_trans(self):
        dict_data = {'sender':''.join(random.sample(string.ascii_letters + string.digits, 8)),
                     'recipient':''.join(random.sample(string.ascii_letters + string.digits, 8)),
                     'amount':random.randrange(1, 10000)}
        return json.dumps(dict_data)

    def gen_block(self, initial_hash=None):
        if initial_hash:
            block = Block()
            block.index = 0
            block.nonce = random.randrange(0, 99999)
            block.previous_hash = '0'
            block.difficulty = 0
            block.transaction_data = self.get_trans()

            guess = str(block.index) + str(block.nonce) + block.previous_hash
            block.hash = hashlib.sha256(guess.encode()).hexdigest()

            block.timestamp = time.time()

            self.chain_list.append(block)
        else:
            for miner in self.miner_list:
                t = MyThread(target=miner.mine, args=(miner,len(self.chain_list),self.get_last_block.get_block_info()['Hash'],
                                                      self.get_trans()))
                t.start()
                t.join()

                self.result_list.append(t.get_result())

            print('All blocks generated by miner:')

            for result in self.result_list:
                print(result[0].get_block_info())

            first_block = self.result_list[0][0]
            min_time = Decimal(self.result_list[0][1])

            for i in range(1, len(self.result_list)):
                if Decimal(self.result_list[i][1]) < min_time:
                    first_block = self.result_list[i][0]

            self.chain_list.append(first_block)
            self.result_list=[]


    def show_chain(self):
        for block in self.chain_list:
            print(block.get_block_info())



