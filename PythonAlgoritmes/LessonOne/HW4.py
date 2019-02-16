# 4. Написать программу, которая генерирует в указанных пользователем границах:
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random as rnd

borderL = input("введите первое значение ")
borderR = input("введите второе значение ")

if (borderL.isdigit()):
    randomValue=rnd.randint(int (borderL), int (borderR))

elif(borderL.isalpha()):
    t=rnd.randint(ord(borderL), ord(borderR))
    randomValue = chr(t)

else:
    randomValue=rnd.uniform(float (borderL), float (borderR))


print (randomValue)