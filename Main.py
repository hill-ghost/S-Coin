from BlockChain import BlockChain

if __name__ == '__main__':
    chain = BlockChain(1)
    for i in range(20):
        chain.gen_block()
    chain.show_chain()
