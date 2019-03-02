#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

array=[-2,-3,-4,-2,-1,-7,-2,-1,-3,-2,-1,-2,-5,-4] 


print (array)
digit=None
index=0
mainindex=0
for i in array:
    if digit is None:
        digit = i
    if i<digit:
        digit = i
        mainindex=index
        index=index+1
    else:
        index=index+1

print (f"число {digit}, с индексом {mainindex} и с позицией {mainindex+1}")
