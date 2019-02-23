# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

num = int(input("Кол-во элементов: "))
ONE=1
def rec(n,x):
    while n>1:
        t=x/-2
        x+=t
        n-=1
        return rec(n,x)
    return x
     
    
print (rec(num,ONE))