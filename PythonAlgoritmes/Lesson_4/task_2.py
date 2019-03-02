# python -m timeit -n 100 -s "import task_2" "task_2.fib(10)"
import cProfile
import functools

# 1. Рекурсия
@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
# "task_2.fib(10)"
# 100 loops, best of 3: 18.4 usec per loop
# "task_2.fib(15)"
# 100 loops, best of 3: 202 usec per loop
# "task_2.fib(20)"
# 100 loops, best of 3: 2.87 msec per loop
# cProfile.run('fib(20)')
# 177/1    0.000    0.000    0.000    0.000 task_2.py:6(fib)    - 10
# 1973/1    0.000    0.000    0.000    0.000 task_2.py:6(fib)   - 15
# 21891/1    0.004    0.000    0.004    0.004 task_2.py:6(fib)  - 20

# 2. Рекрсия + словарь
def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)
# "task_2.fib_dict(10)"
# 100 loops, best of 3: 3.28 usec per loop
# "task_2.fib_dict(20)"
# 100 loops, best of 3: 6.67 usec per loop
# "task_2.fib_dict(100)"
# 100 loops, best of 3: 33.4 usec per loop
# "task_2.fib_dict(200)"
# 100 loops, best of 3: 86.4 usec per loop
# cProfile.run('fib_dict(200)')
# 19/1    0.000    0.000    0.000    0.000 task_2.py:25(_fib_dict)  - 10
# 199/1    0.000    0.000    0.000    0.000 task_2.py:25(_fib_dict) - 100
# 399/1    0.000    0.000    0.000    0.000 task_2.py:25(_fib_dict) - 200

# 3. Цикл
def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for i in range(2, n + 1):
        first, second = second, first + second
    return second
# "task_2.fib_loop(10)"
# 100 loops, best of 3: 0.689 usec per loop
#  "task_2.fib_loop(100)"
# 100 loops, best of 3: 10 usec per loop
# "task_2.fib_loop(100)"
# 100 loops, best of 3: 6.03 usec per loop
# "task_2.fib_loop(1000)"
# 100 loops, best of 3: 62.7 usec per loop
# cProfile.run('fib_loop(100)')
# 1    0.000    0.000    0.000    0.000 task_2.py:46(fib_loop)  - 10


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# test_fib(fib)
# test_fib(fib_dict)
# test_fib(fib_loop)

