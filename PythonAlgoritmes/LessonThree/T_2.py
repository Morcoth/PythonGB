# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить 
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях 
# первого массива стоят четные числа.
import random as rnd
SIZE=10
MIN_LIMIT=1
MAX_LIMIT=100
array = [rnd.randint(MIN_LIMIT, MAX_LIMIT) for _ in range (SIZE)]

index_array=[]
for i in array:
    if i%2==0:
        index = array.index(i)
        index_array.append(index) 
print (array)
print (index_array)