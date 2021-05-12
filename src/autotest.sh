#no=1231
#db="./matchresult.sqlite3"
no=$1
node totoresultforcsv.js ${no}>./results/result${no}.csv
#python3 updateresult.py ${db} ${no}
