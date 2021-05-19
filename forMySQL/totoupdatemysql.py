# -*- coding: utf-8 -*-

import mysql.connector
import pandas as pd
import sys

#tablename = str(sys.argv[1])
csvname = "result1232.csv"

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

#df = pd.read_csv(csvname, header=None)
#print(df)
with open(csvname, 'r', encoding='utf-8') as infile, \
    open('dbchkfile.csv', 'w', encoding='utf-8') as chkfile:
    count = 1
    for line in infile:
        line = line.replace('\n', '')
        print(line)
        # 読み込んだ行の項目を順にカンマ区切りで対応する変数へ文字列としてmapする。
        #year, category, matchname, date, time, home, homescore, awayscore, away, stadium, viewers, live = map(str, line.split(','))
        number, date, stadium, home, away, result= map(str, line.split(','))
        if count > 0:
            #mysql = 'INSERT INTO matches (year, category, matchname, date, time, home, homescore, awayscore, away, stadium, viewers, live) values({},{},{},{},{},{},{},{},{},{},{},{});'.format(year, category, matchname, date, time, home, homescore, awayscore, away, stadium, viewers, live)
            #away = away.replace('\n', '')
            mysql = "SELECT id from matches where home='"+home+"' and away='"+away+"';"
            #print("SELECT id from matches where home='"+home+"' and away='"+away+"';")
            print(mysql)
            cur.execute(mysql)
            #print("cur: "+cur.statement)
            ret=cur.fetchone()
            if not(ret is None):
                if 'id' in ret:
                    print(ret['id'])
                    mysql = 'INSERT IGNORE INTO toto (match_id, number, result) values({},{},{});'.format(ret['id'], number, result)
                    cur.execute(mysql)
                    mysql = "SELECT id from toto where match_id={};".format(ret['id'])
                    cur.execute(mysql)
                    ret=cur.fetchone()
                    mysql = 'UPDATE IGNORE matches SET toto_id={} WHERE home=\'{}\' and away=\'{}\';'.format(ret['id'], home, away)
                    cur.execute(mysql)
            else:
                print("home={}, away={} is not in matches table.".format(home, away))
            # コンソール出力
            #print(u"{}人目の処理を行っています".format(count))
        count = count + 1
    # 項目名列は処理対象の行としてカウントしない
    count = count - 1
    #print(u'{} 件を処理しました。'.format(count))

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