class MyThread(Thread):
    def __init__(self, target, args=()):
        super(MyThread, self).__init__()
        self.func = target
        self.arg = args

    def run(self):
        self.result = self.func(*self.arg)

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            print('自定义线程获取结果时发生了错误:', e)
            return None
