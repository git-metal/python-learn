
import threading

class Country():

    def __init__(self, name, id):
        self.name = name
        self.id = id

g_local_thread = threading.local()


def thread_func(name, id):
    c = Country(name, id)
    g_local_thread.country = c
    test()

def test():
    print("thread:%s name=%s id=%s" % (threading.currentThread().getName(), g_local_thread.country.name, g_local_thread.country.id))


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_func, args=("china", "14",))
    t2 = threading.Thread(target=thread_func, args=("india", "15",))
    t1.start()
    t2.start()
    t2.join()