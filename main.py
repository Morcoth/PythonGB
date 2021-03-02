import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import re
import os
# Реализовать сценарий загрузки архивных CorpId и SsoId из лог-файлов продуктивного контура
# При анализе логов необходимо отталкиваться от ЕНО (ServiceNumber). По ЕНО осуществлять поиск обращения в базе ОВГИ (Recourse). В обращении заполнять  CorpId и SsoId значениями из блока Представитель xml сообщения, если представитель отсутствует - то из блока Заявитель.

# Пример ссылки на папку с логами обращений за 24.02
# \\ovga2-logs\Ovga\MqLogs\2021\02\24\In\Request\

def updateTable(eno, corpId, ssoId):
    try:
        connection = pg.connect(dbname='op_dev_morcoth', user='postgres', 
                        password='123', host='localhost', port='5433')

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from recource where service_number = %s"""
        cursor.execute(sql_select_query, (eno,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_corpId = """Update recource set CorpId = %s where service_number = %s"""
        cursor.execute(sql_update_corpId, (corpId, eno))
        sql_update_ssoId = """Update recource set CorpId = %s where service_number = %s"""
        cursor.execute(sql_update_ssoId, (ssoId, eno))

        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from recource where service_number = %s"""
        cursor.execute(sql_select_query, (eno,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



patternEno = re.compile("<ns1:ServiceNumber>(.+?)<\/ns1:ServiceNumber>")
patternCorpId = re.compile("<ns1:CorpId>(.+?)<\/ns1:CorpId>")
patternSsoId = re.compile("<ns1:SsoId>(.+?)<\/ns1:SsoId>")

directory = r'2020'
for i,j,y in os.walk(directory):
    print(i) 
    if "Request" in i:
        recourceEno = ''
        recourceCorpId = ''
        recourceSsoId = ''
        #   print(os.path.join(directory, filename))
        for filename in os.listdir(i):
            for t, line in enumerate(open(os.path.join(i, filename))):
                    for match in re.finditer(patternEno, line):
                        recourceEno = match.group(1)
                    for match2 in re.finditer(patternCorpId, line):
                        recourceCorpId = match2.group(1)
                    for match3 in re.finditer(patternSsoId, line):
                        recourceSsoId = match3.group(1)
            print (f'Eno = {recourceEno} CorpId = {recourceCorpId} SsoId = {recourceSsoId}')
    else:
        continue



# eno = '0001-9000003-020301-0027253/21'
# corpId = 'f7f4a381-eb93-571b-3ca9-7729a8a840eb'
# updateTable(eno, corpId)
