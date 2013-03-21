# This demonstrates simple usage of the multiprocessing
# library in python.

import multiprocessing

class Example:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hello(self):
        print(self.a)
        print(self.b)
    
obj1 = Example('obj1', '1')
obj2 = Example('obj1', '2')

def worker(o):
    """thread worker function"""
    o.hello()
    return

if __name__ == '__main__':
    p = multiprocessing.Process(target=obj1.hello)
    p.start()
    p2 = multiprocessing.Process(target=obj2.hello)
    p2.start()
    p.join()
    p2.join()
    print("main thread")
