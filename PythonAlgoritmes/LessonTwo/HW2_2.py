#2 Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def Init ():
    inputnum = input ("Ввдите число: ") 
    ch=0
    nch=0
    for i in inputnum:
        if (int(i)%2==0):
            ch+=1
        else:
            nch+=1
    print (f"четных = {ch}, нечетных = {nch}")

Init()