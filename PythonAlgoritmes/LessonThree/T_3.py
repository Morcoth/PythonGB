#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as rnd
SIZE=10
MIN_LIMIT=1
MAX_LIMIT=100
array = [rnd.randint(MIN_LIMIT, MAX_LIMIT) for _ in range (SIZE)]
print (array)

max_elem=0
min_elem=0

for i in array:
    if i>max_elem:
        max_elem=i
        if min_elem==0:
            min_elem=i
    elif i<min_elem:
        min_elem=i


array[array.index(min_elem)], array[array.index(max_elem)] = array[array.index(max_elem)], array[array.index(min_elem)] 
print (array)


