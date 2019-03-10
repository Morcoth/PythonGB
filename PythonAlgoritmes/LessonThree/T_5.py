#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import sys
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
tzero = ()
tup = (array, digit, index, mainindex, )

print (f"число {digit}, с индексом {mainindex} и с позицией {mainindex+1}")
print (array.__class__, sys.getsizeof(array), array)
# переменная array с числами внутри занимает 176 байт
print (digit.__class__, sys.getsizeof(digit), digit)
# переменная digit занимает 28 байт
print (tup.__class__, sys.getsizeof(tup)- sys.getsizeof(tzero), tup)
#объединенный кортеж со всеми элементами занимает 32 байта (наверное потому что там ссылки на яейки памяти поэтому не считает правильно)