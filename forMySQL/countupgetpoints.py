# -*- coding: utf-8 -*-

import mysql.connector
import pandas as pd
import sys

#tablename = str(sys.argv[1])
csvname = "result1232.csv"
#総得点を出したいチーム名
target = str(sys.argv[1])

# 接続する 
conn =  mysql.connector.connect(
    host="localhost",
    database="toto",
    user="root",
    password="root"
)

print("connection: "+str(conn.is_connected()))
# カーソルを取得する
cur = conn.cursor(buffered=True, dictionary=True)
mysql = "SELECT SUM(IF( home='"+target+"' , homescore , IF( away='"+target+"' , awayscore , 0))) FROM matches;"
cur.execute(mysql)
ret=cur.fetchone()
mysql = "SUM(IF( home='"+target+"' , homescore , IF( away='"+target+"' , awayscore , 0)))"
#print(ret)
print(ret[mysql])

conn.commit()
cur.close()
conn.close()