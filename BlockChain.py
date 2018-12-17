class BlockChain(object):
    def __init__(self, hash_num):
        self.chain_list = []

        self.miner_list = []

        for i in range(6):
            self.miner_list.append(Miner)

            self.result_list = []

            self.gen_block(hash_num)
            
