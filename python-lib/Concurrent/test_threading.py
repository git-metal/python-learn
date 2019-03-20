
import threading
from time import ctime, sleep


class MyThread(threading.Thread):

    def __init__(self, func, args, name=""):
        # threading.Thread.__init__(self)
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print("run MyThread")
        self.func(*self.args)


def music(name):
    for i in range(2):
        print("I was listening to %s. %s" % (name, ctime()))
        sleep(1)
    pass


def move(name):
    for i in range(2):
        print("I was at the %s! %s" % (name, ctime()))
        sleep(1)


def super_play(file, time):
    for i in range(2):
        print('Start playing: %s! %s' % (file, ctime()))
        sleep(time)


if __name__ == "__main__":
    threads = []
    t1 = threading.Thread(target=music, args=("光年之外",))
    threads.append(t1)
    t2 = threading.Thread(target=move, args=("正义联盟",))
    threads.append(t2)

    # test Thread function
    for t in threads:
        t.start()
    t1.join()
    t2.join()
    print("end: %s" % ctime())
    print(super_play.__name__)

    # test Thread Class
    in_list = {'光年之外': 3, '正义联盟': 5}
    threads = []
    for k, v in in_list.items():
        t = MyThread(super_play, (k, v), super_play.__name__)
        threads.append(t)
    for t in threads:
        t.start()

    sleep(5)
