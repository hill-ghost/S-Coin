class Block(object):
    def __init__(self):
        self.index = None #序号
        self.hash = None #区块id
        self.previous_hash = None #上一个区块的id
        self.nonce = None #随机数
        self.difficulty = None #难度系数
        self.timestamp = None #时间戳
        self.transaction_data = None #交易信息

    def get_block_info(self):
        block_info = {
        'Index':self.index,
        'Hash':self.hash,
        'Previous_hash':self.previous_hash,
        'Nonce':self.nonce,
        'Difficulty':self.difficulty,
        'Timestamp':self.timestamp,
        'Transaction_data':self.transaction_data
        }
        return block_info
