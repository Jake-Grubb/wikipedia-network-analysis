import time
from multiprocessing import Pipe

def init(ptw):
    print("writer begin")

    while(True):
        print(ptw.recv())