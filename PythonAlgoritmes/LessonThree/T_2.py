# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить 
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях 
# первого массива стоят четные числа.
import random as rnd
import sys
SIZE=10
MIN_LIMIT=1
MAX_LIMIT=100
x1=sys.getsizeof(MIN_LIMIT)
x2=sys.getsizeof(MAX_LIMIT)
x3=sys.getsizeof(SIZE)
print (MIN_LIMIT.__class__, sys.getsizeof(MIN_LIMIT), MIN_LIMIT)
print (MAX_LIMIT.__class__, sys.getsizeof(MAX_LIMIT), MAX_LIMIT)
print (SIZE.__class__, sys.getsizeof(SIZE), SIZE)

array = [rnd.randint(MIN_LIMIT, MAX_LIMIT) for _ in range (SIZE)]
print (array.__class__, sys.getsizeof(array), array)
x4=sys.getsizeof(array)
level = 0
index_array=[]
for i in array:
    if i%2==0:
        index = array.index(i)
        index_array.append(index) 
print (array)
t = sys.getsizeof([])
print (array.__class__, sys.getsizeof(array)-t, array)
x5=sys.getsizeof(array)-t
#суммарное количетво выделенной памяти без учета памяти выделенной под массив для первого массива равна 128
print (index_array)
print (index_array.__class__, sys.getsizeof(index_array)-t, index_array)
x6=sys.getsizeof(index_array)-t
#суммарное количетво выделенной памяти без учета памяти выделенной под массив для  массива индексов равна 32
#Python 3.7.2.64-bit
#OS type 64 bit
print (x1+x2+x3+x4+x5+x6)
#Всего было выделено 468 байт под переменные


