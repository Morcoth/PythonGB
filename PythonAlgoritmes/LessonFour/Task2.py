import math
import timeit
import cProfile


def foo(n):
    dictind = {}
    keys_for_dict=1
    for i in range(2, 10000):
        flag = True
        for j in range(2, 1 + int(math.sqrt(i))):
            if not i % j:
                flag = False
                break
        if flag:
            dictind.update({keys_for_dict:i})
            keys_for_dict=keys_for_dict+1
    print (f"{n}= {dictind.get(n)}")


def main(n):
    foo(50)   

#cProfile.run('main(1000)')

#  1    0.015    0.015    0.018    0.018 Task2.py:6(foo)
print(timeit.timeit("foo(50)", 'from __main__ import foo', number=100))
# 1.9100934669995695 для 100 вызовов