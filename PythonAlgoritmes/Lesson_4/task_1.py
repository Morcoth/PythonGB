import time
import timeit
import cProfile

start = time.time()
lst = [i for i in range(100000)]
delta = time.time() - start
print(delta)

# print(timeit.timeit('lst = [i for i in range(100000)]', number=100))

spam = """
for i in range(10):
    x = i**2
    y = i**0.5
"""

# print(timeit.timeit(spam, number=100))


def get_len(array):
    return len(array)


def get_sum(array):
    sum_ = 0
    for item in array:
        sum_ += item
    return sum_


def main(n):
    lst = [i for i in range(n)]
    len_ = get_len(lst)
    sum_ = get_sum(lst)

cProfile.run('main(10000000)')
