import time
import writer
import multiprocessing as mp
from multiprocessing import Pipe

def createEdge(s,t):
        return '\'' + s + '\'' + ',' + '\'' + t + '\''

def init(iq, ql, oset, sl, rtp):
        print("parser begin")

        ptw_par, ptw_wri = mp.Pipe()
        wri = mp.Process(target=writer.init, args=(ptw_wri,))

        wri.start()
        info = rtp.recv()
        while(info != 'KILL'):
                sl.acquire()
                a = False
                edgeList = set()
                for x in info.links:
                        if(x[0] != 'a' and x[0] != 'A' and a == True):
                                break
                        elif (x[0] == 'a' or x[0] == 'A'):
                                a = True
                                edge = createEdge(info.title,x)
                                edgeList.add(edge)
                                ptw_par.send(edge)
                                if(x not in oset):
                                        ql.acquire()
                                        iq.put(x)
                                        oset.append(x)
                                        ql.release()
                sl.release()
                info = rtp.recv()

        ptw_par.send('KILL')
        wri.join()
