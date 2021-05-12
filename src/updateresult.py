import sqlite3
import pandas as pd
import sys

dbname="./matchresult.sqlite3"
tablename = str(sys.argv[1])

#dbname = str(sys.argv[1])
#tablename = str(sys.argv[2])

conn = sqlite3.connect(dbname)
cur = conn.cursor()

# pandasでカレントディレクトリにあるcsvファイルを読み込む
# csvには、1列目にyear, 2列目にmonth, 3列目にdayが入っているとする。
csvname = "result"+tablename+".csv"
df = pd.read_csv(csvname, header=None)
print(csvname)

# カラム名（列ラベル）を作成。csv file内にcolumn名がある場合は、下記は不要
# pandasが自動で1行目をカラム名として認識してくれる。
df.columns = ['date', 'stadium', 'No', 'home', 'points', 'away', 'result']

# dbのnameをsampleとし、読み込んだcsvファイルをsqlに書き込む
# if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
df.to_sql(tablename, conn, if_exists='replace')

cur.close()
conn.close()