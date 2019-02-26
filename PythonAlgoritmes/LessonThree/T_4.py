#  4. Определить, какое число в массиве встречается чаще всего.

array=[2,3,4,2,1,7,2,1,3,2,1,2,5,4,]

print (array)

max_meet_num=0
digit=0
for i in array:
    if array.count(i) >max_meet_num:
        max_meet_num = array.count(i)
        digit = i

print (f"наиболее часто встречается {digit}, {max_meet_num} раз")