#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict, namedtuple, deque


Organisation =  namedtuple('Organisation', 'name, date_profit, mid')

def create_org():
   orgname = input("Введите название организации:  ")
   orgprof = {}
   quart=1
   mid =float(0)

   while quart<=4:
       inp= float(input(f'Введите прибыль за {quart} квартал: '))
       orgprof[(quart)] =inp
       mid = mid + inp
       quart+=1
   mid = mid/4
   organisation = Organisation(orgname,  orgprof, mid)

   print (organisation)
   return organisation

        
id = 0
orglistdeque=deque(maxlen=2)
while id<2:
    _org=create_org()
    orglistdeque.append(_org)
    id+=1

profforall=0
for t in orglistdeque:
    org_prof=0
    for prof in t.date_profit:
        profforall+=t.date_profit[prof]
    midprof = profforall/4
    if  t.mid<midprof:
        print (f"организация {t.name} показала доходность ниже среднего по больнице")
    else:
        print (f"организация {t.name} показала доходность выше среднего по больнице")