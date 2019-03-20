from concurrent.futures import ProcessPoolExecutor,wait,as_completed
import urllib.request
URLS = ['http://www.163.com', 'https://www.baidu.com/', 'https://github.com/']
def load_url(url):
    with urllib.request.urlopen(url, timeout=60) as conn:
        print('%r page is %d bytes' % (url, len(conn.read())))

executor = ProcessPoolExecutor(max_workers=3)

if __name__ == '__main__':

    f_list = []
    for url in URLS:
        future = executor.submit(load_url,url)
        f_list.append(future)
        print(future.done())
    # executor.map(load_url, URLS)
    print(wait(f_list))
    print('主线程')
