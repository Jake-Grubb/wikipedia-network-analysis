import wikipedia as wiki
import time

class Page:
        title = None
        links = []

def init(iq, ql, oset, sl, rtp, err):
        print("retriever begin")

        while(True):
                left = 5
                print("here 1")
                while(left > 0):
                        ql.acquire()
                        while(not iq.empty()):
                                ql.release()
                                left = 5
                                p = Page()          
                                ql.acquire()                      
                                p.title = iq.get()
                                ql.release()
                                try:
                                        p.links = wiki.page(p.title).links
                                        rtp.send(p)
                                except:
                                        print("gotcha bitch")
                                        pass
                                ql.acquire()
                        ql.release()
                        time.sleep(1)
                        left -= 1
                err.send('QUEUE_EMPTY')
                e = err.recv()
                if(e != 'CONTINUE'):
                        rtp.send('KILL')
                        break
