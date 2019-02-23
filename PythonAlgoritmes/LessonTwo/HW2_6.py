# В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
#  Если за 10 попыток число не отгадано, то вывести загаданное число.

import random as rnd

num = rnd.randint(0, 100)
win=False
def game (num , TRY_COUNT, win):
    while (TRY_COUNT>0 or win!=True):
        if (TRY_COUNT==0 ):
            print (f"Попыьки кончились, это было число {num}")
            break
        user_num = int(input("Введите число: "))
        if(user_num==num):
            win=True
            break
        elif (user_num>num):
            TRY_COUNT-=1
            print ("Число меньше")
            game (num, TRY_COUNT, win)
        elif (user_num<num):
            TRY_COUNT-=1
            print ("Число больше")
            game (num, TRY_COUNT, win)
        if (TRY_COUNT>0 and win == True):
            print ("Победа")
            break
        break
    
        
game (num, 10, win)
