from multiprocessing import Process, Queue, Pool
import os, time
from time import sleep

#test how many process can be handled simultaneously
#16 processes can be handled simultaneously
def long_time_task(name):
    print ('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(3)
    end = time.time()
    print ('Task %s runs %0.2f seconds.' % (name, (end - start)))

#add to the queue
def put(q):
    for i in range(8):
        q.put(str(i))
        print('put %s' % i)
    q.put(None)
    print ('put is done')

#read and delete from the queue
def get(q):
	while True:
		info = q.get()
		print ('get %s' % info)
		if not info:
			break
		sleep(1)

#n is the number of processes
def main(n):
    print ('Parent process %s.' % os.getpid())
    start = time.time()
    p = Pool()
    for i in range(n):
        p.apply_async(long_time_task, args=(i,))
    print ('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print ('All subprocesses done.')
    end = time.time()
    print("总共用时{}秒".format((end - start)))
    print('main task start')
    q = Queue()
    p1 = Process(target=put, args=(q, ))
    p2 = Process(target=get, args=(q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print ('main task done')
    
if __name__ == '__main__':
	main(17)