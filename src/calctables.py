import sqlite3
import pandas as pd
import sys

dbname = "./matchresult.sqlite3"

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# table一覧の取得
tables = []
cur.execute("select * from sqlite_master where type='table'")
for row in cur.fetchall():
    tables.append(row[1])
print(tables)

# totalテーブルがなかったら作成(J1のみ)
J1 = [
"札幌", "仙台","鹿島", "浦和", "柏",
"Ｆ東京","川崎", "横浜Ｍ","横浜Ｃ","湘南", 
"清水","名古屋","Ｇ大阪","Ｃ大阪","神戸", 
"広島", "徳島", "福岡", "鳥栖", "大分" 
]
cur.execute("SELECT * FROM sqlite_master WHERE type='table' and name='total'")
if not cur.fetchone():
    cur.execute('CREATE TABLE total (id int, name text, win int, lose int, draw int, getp int, lossp int)')
    cur.execute('INSERT INTO total VALUES (0, "札幌", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (1, "仙台", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (2, "鹿島", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (3, "浦和", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (4, "柏", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (5, "Ｆ東京", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (6, "川崎", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (7, "横浜Ｍ", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (8, "横浜Ｃ", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (9, "湘南", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (10, "清水", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (11, "名古屋", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (12, "Ｇ大阪", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (13, "Ｃ大阪", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (14, "神戸", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (15, "広島", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (16, "徳島", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (17, "福岡", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (18, "鳥栖", 0, 0, 0, 0, 0)')
    cur.execute('INSERT INTO total VALUES (19, "大分", 0, 0, 0, 0, 0)')
    conn.commit()

# 第何回のテーブルの検索
for id,team in enumerate(J1):
    getpoints = [] #得点のリスト
    losspoints = [] #失点のリスト
    getpoint=0 #総得点
    losspoint=0 #総失点
    win=0 #勝利数
    lose=0 #敗北数
    draw=0 #引き分け数
    for i in range(len(tables)):
        #テーブルtotalは飛ばす
        if(tables[i]=='total'):
            continue
        sql = "SELECT * FROM sqlite_master WHERE type='table' and name='"+tables[i]+"'"
        cur.execute(sql)
        if cur.fetchone():
            #print(tables[i])
            sql = "SELECT * FROM '"+tables[i]+"'"
            cur.execute(sql)
            for row in cur.fetchall():
                #print(row)
                #homeチームだったとき
                if row[4]==team:
                    idx=row[5].find('-')
                    getpoints.append(row[5][:idx])
                    getpoint += int(row[5][:idx])
                    losspoints.append(row[5][idx+1:])
                    losspoint += int(row[5][idx+1:])
                    #print("home: "+row[4]+": "+row[5]+", "+row[5][:idx])
                    #勝敗の確認
                    if row[7]==0:
                        draw+=1
                    if row[7]==1:
                        win+=1
                    if row[7]==2:
                        lose+=1
                #awayチームだったとき
                if row[6]==team:
                    idx=row[5].find('-')
                    losspoints.append(row[5][:idx])
                    losspoint += int(row[5][:idx])
                    getpoints.append(row[5][idx+1:])
                    getpoint += int(row[5][idx+1:])
                    #print("away: "+row[6]+": "+row[5]+", "+row[5][:idx])
                    #勝敗の確認
                    if row[7]==0:
                        draw+=1
                    if row[7]==1:
                        lose+=1
                    if row[7]==2:
                        win+=1


    print(str(id)+":"+str(team)+": get="+str(getpoint)+": ", end='')
    print(getpoints)
    print(str(id)+":"+str(team)+": loss="+str(losspoint)+": ", end='')
    print(losspoints)
    print(str(id)+":"+str(team)+": win="+str(win)+", lose="+str(lose)+", draw="+str(draw))

    #総得点の反映
    cur.execute("UPDATE total SET getp=?, lossp=? WHERE id=?", (int(getpoint),int(losspoint),int(id)))
    #勝利数の反映
    cur.execute("UPDATE total SET win=?, lose=?, draw=? WHERE id=?", (int(win),int(lose),int(draw),int(id)))

conn.commit()
cur.close()
conn.close()