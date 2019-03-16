#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.
import random as rnd

array = [rnd.uniform(0, 50.01) for _ in range (10)]
print (array)

def mergeSort(array):
    if len(array)>1:    
        midarray = len(array)//2
        lefthalf = array[:midarray]
        righthalf = array [midarray:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j ,k=0,0,0

        while i < len(lefthalf) and j < len(righthalf):
               if lefthalf[i] < righthalf[j]:
                   array[k]=lefthalf[i]
                   i=i+1
               else:
                   array[k]=righthalf[j]
                   j=j+1
               k=k+1

        while i < len(lefthalf):
               array[k]=lefthalf[i]
               i=i+1
               k=k+1

        while j < len(righthalf):
               array[k]=righthalf[j]
               j=j+1
               k=k+1

mergeSort(array)
print(array)