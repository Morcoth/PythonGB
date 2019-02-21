# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.  Числа и знак операции вводятся пользователем. 
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
#  Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
def OperationInput (first_num, second_num, rightInput):
    if (rightInput==False):
        print( "Повторите ввод оператора")
    
    return   input (f"что вы хотите сделать с числами {first_num} и {second_num}:")

def mat():
    while(True):
        right = True
        first_num = int(input("First num: "))
        second_num = int(input("Second num: "))
        operator =OperationInput(first_num, second_num, right)
        operations(first_num, second_num, operator)
        
        
        
def operations(first_num, second_num, operator):
    if(operator=="+"):
        print ("Сумма чисел =", first_num+second_num)
    elif (operator=="-"):
         print ("Разница двух чисел = ", abs(first_num+second_num))
    elif (operator=="*"):
         print ("Разница двух чисел =", first_num*second_num)
    elif (operator=="/"):
        if(second_num==0):
            print ("На ноль делить нельзя")
        else:
            print ("Деление двух чисел = ", first_num/second_num)
    else:
        right=False
        operator=OperationInput(first_num, second_num, right)
        operations(first_num, second_num, operator)

mat()


