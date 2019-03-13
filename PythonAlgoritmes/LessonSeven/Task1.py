#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный
#  случайными числами на промежутке [-100; 100). 
# Выведите на экран исходный и отсортированный массивы. 
# Сортировка должна быть реализована в виде функции. 
# По возможности доработайте алгоритм (сделайте его умнее).
import random as rnd

array = [rnd.randint(-100, 101) for _ in range (10)]
print (array)
def array_bubble_sort (array):
    for i in range(len(array) -1):
        cnt=0
        for j in range(len(array) - 1 - cnt ):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                cnt+=1

        
    return array

print(array_bubble_sort(array))