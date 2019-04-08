import time
from multiprocessing import Pipe

def init(ptw):
    print("writer begin")

    sfile = open("edges.csv","a+")

    while(True):
        edge = ptw.recv()
        if(edge != 'KILL'):
            sfile.write(edge + '\n')
        else:
            break
    
    sfile.close()