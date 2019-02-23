#Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. 
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

STARTCODE = 32
ENDCODE = 128

for i in range (STARTCODE, ENDCODE):    
    print (STARTCODE, chr(STARTCODE))
    STARTCODE+=1
    if i%10==0:
        print ()


