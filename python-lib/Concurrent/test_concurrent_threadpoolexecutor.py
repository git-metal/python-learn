# 参考 https://www.cnblogs.com/dylan-wu/p/7163823.html

from concurrent.futures import ThreadPoolExecutor
import urllib.request

URLS = ['http://www.163.com', 'https://www.baidu.com/', 'https://github.com/', 'https://pypi.org/']

def load_url(url):
    with urllib.request.urlopen(url, timeout=60) as conn:
        print('%r page is %d bytes' % (url, len(conn.read())))

executor = ThreadPoolExecutor(max_workers=3)

# for url in URLS:
#     future = executor.submit(load_url,url)
#     print(future.done())

executor.map(load_url, URLS)

print('主线程')