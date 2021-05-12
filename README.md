# Docker-mysql-phpmyadmin_node-express
Dockerでmysplとphpmyadmin環境を準備してnode.jsからDBデータを参照する
<br><br><br>

## 手順
**1. Docker環境を構築する（MySQLとphpMyAdminのインストールと起動）**  
$ `docker-compose up -d`  

**2. phpMyAdminへのアクセス**  
http://localhost:8080/  

**3. npmのモジュールをインストール（expressとmysql）**  
$ `npm i`  

**4. 各jsファイルからNodeのWebサーバーを立ち上げてブラウザからアクセスして動作を確認する**  
* Webサーバー立ち上げを確認 - 「hello world」  
$ `node index.js`  
http://localhost:1234/  

* Docker - mysqlのDB情報を取得し、返す
$ `node index_database.js`  

* express経由？でWebサーバーで表示  
$ `node index_express.js`  
http://localhost:3000/  

* Docker - mysqlのDB情報を取得・Webサーバーで表示  
$ `node index_express_database.js`  
http://localhost:3000/  



-----
docker-compose ps  
docker-compose stop  
docker-compose down  
npm ls --depth=0

-----
◆docker-compose でMySQL環境簡単構築 - Qiita
https://qiita.com/A-Kira/items/f401aea261693c395966



