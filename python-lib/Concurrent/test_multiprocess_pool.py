import multiprocessing
from multiprocessing import Pool, TimeoutError
import time
import os


def test(msg):
    print("pid:{0} name:{1} msg:{2}".format(os.getpid(), multiprocessing.current_process().name, msg))

def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))

def test_process():
    print('Parent process {0} is Running'.format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=test, args=(str(i),))
        print('process start')
        p.start()
    p.join()
    print('Process close')


def test_pool():
    print('current process {0}'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')

if __name__ == '__main__':
    # test_process()
    test_pool()
