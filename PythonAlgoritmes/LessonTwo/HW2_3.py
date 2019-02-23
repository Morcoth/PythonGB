#3. Сформировать из введенного числа обратное по порядку входящих в него цифр 
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

def Init ():
    inputnum = int(input ("Ввдите число: ")) 
    result = 0
    while inputnum>0:
        result = result*10 + inputnum%10
        inputnum = inputnum//10
    print(result)
Init()