# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a = ord(input('1-ая буква: '))
b = ord(input('2-ая буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
c = abs(a-b)-1
print(' %d-ое и %d-ое место' % (a,b))
print('Между буквами %d символа(ов)' %c)