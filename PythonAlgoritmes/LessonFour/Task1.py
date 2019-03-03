# -*- coding: utf-8 -*-


# Задание 1 из 3его урока. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# import timeit
# import cProfile


def mat (i):
    count = 0
    while i<10:
        for y in range (2,100):
            if y%i==0:
                count=count+1
        #print (i, count) 
        i=i+1            
        mat(i)
        return None 
def main(n):
    mat(2)

#print(timeit.timeit("mat(2)", 'from __main__ import mat', number=100))
#0.014456499999999983
# 1.125776 с выводом значений
#cProfile.run('main(10000000)')
#C Принтом        
        #100 loops, best of 3: 89.2 usec per loop
        #1000 loops, best of 3: 92.4 usec per loop
        #10000 loops, best of 3: 98.3 usec per loop
        #100000 loops, best of 3: 103 usec per loop
#Без принта
        #100000 loops, best of 3: 35.7 usec per loop
def mat2 ():
    for i in range (2,10):
            count=0
            for y in range (2,100):
                    if y%i==0:
                             count=count+1
            #print (i, count)
def main2(n):
    mat2()
#print(timeit.timeit("mat2()", 'from __main__ import mat2', number=100))
#0.01600669999999993 без вывода значений
# 1.3244124999999998 с выводом значений

#cProfile.run('main2(10000000)')
#100 loops, best of 3: 70.6 usec per loop
#1000 loops, best of 3: 77.9 usec per loop
#10000 loops, best of 3: 94.8 usec per loop
#100000 loops, best of 3: 100 usec per loop