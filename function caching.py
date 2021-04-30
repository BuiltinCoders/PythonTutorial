import time
from functools import lru_cache

@lru_cache(maxsize=10)
def some_work(n):
    time.sleep(n)
    return n

some_work(3)
print('some work called')
some_work(2)
print('some work called again')
some_work(1)
print('some work called again..')
some_work(3)
print('called again n==3')
some_work(6)
print('secondlast call')
some_work(6)
print('last call')