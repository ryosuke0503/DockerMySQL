# -*- coding: utf-8 -*-

import mysql.connector
import pandas as pd
import sys

#tablename = str(sys.argv[1])

# 接続する 
conn =  mysql.connector.connect(
    host="localhost",
    database="test_database",
    user="root",
    password="root"
)

print("connection: "+str(conn.is_connected()))
# カーソルを取得する
cur = conn.cursor()

sql = "select id, name from test_table"
cur.execute(sql)

# 実行結果を取得する
rows = cur.fetchall()

# 一行ずつ表示する
for row in rows:
 print(row)

#csvname = "result"+tablename+".csv"
#df = pd.read_csv(csvname, header=None)
#print(csvname)

#df.columns = ['date', 'stadium', 'No', 'home', 'points', 'away', 'result']
#df.to_sql(tablename, conn, if_exists='replace')

conn.commit()
cur.close()
conn.close()