import psycopg2 as pg
import configparser 
import re
import os

def updateTable(eno, corpId, ssoId):
    try:
        connection = pg.connect(dbname='1', user='1', 
                        password='1', host='112', port='1')

        cursor = connection.cursor()

        # print("Table Before updating record ")
        # sql_select_query = """select * from recourse where eno = %s"""
        # cursor.execute(sql_select_query, (eno,))
        # record = cursor.fetchone()
        # print(record)

        # Update single record now
        sql_update_corpId = """Update recourse set corpid = %s where eno = %s"""
        cursor.execute(sql_update_corpId, (corpId, eno))
        sql_update_ssoId = """Update recourse set sso_id = %s where eno = %s"""
        cursor.execute(sql_update_ssoId, (ssoId, eno))

        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        # print("Table After updating record ")
        # sql_select_query = """select * from recourse where eno = %s"""
        # cursor.execute(sql_select_query, (eno,))
        # record = cursor.fetchone()
        # print(record)

    except (Exception, pg.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
# config = configparser.ConfigParser()
# config.read("../config.ini") 
# print(config["general"]["dbname"])

patternEno = re.compile("<ns1:ServiceNumber>(.+?)<\/ns1:ServiceNumber>")
patternCorpId = re.compile("<ns1:CorpId>(.+?)<\/ns1:CorpId>")
patternSsoId = re.compile("<ns1:SsoId>(.+?)<\/ns1:SsoId>")

directory = r'.'
for i,j,y in os.walk(directory):
    print(i) 
    if "Request" in i:
        recourseEno = ''
        recourseCorpId = ''
        recourseSsoId = ''
        #   print(os.path.join(directory, filename))
        for filename in os.listdir(i):
            for t, line in enumerate(open(os.path.join(i, filename), encoding='utf-8')):
                    for match in re.finditer(patternEno, line):
                        recourseEno = match.group(1)
                    for match2 in re.finditer(patternCorpId, line):
                        recourseCorpId = match2.group(1)
                    for match3 in re.finditer(patternSsoId, line):
                        recourseSsoId = match3.group(1)
            print (f'Eno = {recourseEno} CorpId = {recourseCorpId} SsoId = {recourseSsoId}')
            updateTable(recourseEno, recourseCorpId, recourseSsoId)

    else:
        continue



# eno = '0001-9000003-020301-0027253/21'
# corpId = 'f7f4a381-eb93-571b-3ca9-7729a8a840eb'
# updateTable(eno, corpId)
