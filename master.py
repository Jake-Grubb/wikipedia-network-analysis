import retriever
import parser
import multiprocessing as mp
import wikipedia as wiki
import sys

def fetchRand(oset):
        first = wiki.random()
        while((first[0] != 'a' and first[0] != "A") or first in oset):
            first = wiki.random()

        return first

def resume():
    inQueue = mp.Queue()
    manager = mp.Manager()
    outset = manager.list()

    qfile = open("queue.txt")
    sfile = open("set.txt")

    for line in qfile:
        inQueue.put(line)
    
    for line in sfile:
        outset.append(line)

    return inQueue, outset

def dump(q, s):
    qfile = open("queue.txt", "a+")
    sfile = open("set.txt", "a+")

    while(not q.empty()):
        qfile.write(q.get() + '\n')

    for x in s:
        sfile.write(x + '\n')

if(__name__ == '__main__'):
    inQueue = mp.Queue()

    rtp_ret, rtp_par = mp.Pipe()
    err_mas, err_ret = mp.Pipe()

    manager = mp.Manager()
    outset = manager.list()

    qlock = mp.Lock()
    slock = mp.Lock()

    ret = mp.Process(target=retriever.init, args=(inQueue,qlock,outset,slock,rtp_ret,err_ret,))
    par = mp.Process(target=parser.init, args=(inQueue,qlock,outset,slock,rtp_par,))


    try:
        if(len(sys.argv) == 1):
            first = fetchRand(outset)
            inQueue.put(first)
            outset.append(first)
        else:
            inQueue, outset = resume()

        ret.start()
        par.start()
        while(True):
            err_mess = err_mas.recv()
            if(err_mess == 'QUEUE_EMPTY'):
                qlock.acquire()
                slock.acquire()
                next = fetchRand(outset)
                inQueue.put(next)
                outset.append(next)
                slock.release()
                qlock.release()
                err_mas.send('CONTINUE')
            else:
                print(err_mess)

        ret.join()
        par.join()
    except:
        print('An exception occured')
        dump(inQueue, outset)    
    