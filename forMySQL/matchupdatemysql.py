# -*- coding: utf-8 -*-

import mysql.connector
import pandas as pd
import sys

#tablename = str(sys.argv[1])
csvname = "J1_2020_2.csv"

# 接続する 
conn =  mysql.connector.connect(
    host="localhost",
    database="toto",
    user="root",
    password="root"
)

print("connection: "+str(conn.is_connected()))
# カーソルを取得する
cur = conn.cursor()

#df = pd.read_csv(csvname, header=None)
#print(df)
with open(csvname, 'r', encoding='utf-8') as infile, \
    open('dbchkfile.csv', 'w', encoding='utf-8') as chkfile:
    count = 1
    print(infile)
    for line in infile:
        # 読み込んだ行の項目を順にカンマ区切りで対応する変数へ文字列としてmapする。
        year, category, matchname, date, time, home, homescore, awayscore, away, stadium, viewers, live = map(str, line.split(','))
        if count > 0:
            mysql = 'INSERT IGNORE INTO matches (year, category, matchname, date, time, home, homescore, awayscore, away, stadium, viewers, live) values({},{},{},{},{},{},{},{},{},{},{},{});'.format(year, category, matchname, date, time, home, homescore, awayscore, away, stadium, viewers, live);
            print(mysql)
            cur.execute(mysql)
 
            # コンソール出力
            print(u"{}人目の処理を行っています".format(count))
        count = count + 1
    # 項目名列は処理対象の行としてカウントしない
    count = count - 1
    print(u'{} 件を処理しました。'.format(count))

    # 確認用に操作中テーブルからレコード取得
    cur.execute('select * from matches;')
    rows = cur.fetchall()

    # 取得したレコードを外部出力。
    for row in rows:
        # エラーが出るため数値は文字へ一旦変換
        row_str = map(str,row)
        # 出力
        print(','.join(list(row_str)), file=chkfile)

conn.commit()
cur.close()
conn.close()