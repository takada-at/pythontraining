## INSTALL
python 練習用のWebアプリケーションテンプレートです。

### 1. Create Database Auth File
```sql
CREATE DATABASE bbs DEFAULT character set=utf8;
GRANT ALL ON bbs.* TO bbs IDENTIFIED BY PASSWORD('password');
FLUSH PRIVILEGES;
```

```bash
$ echo "bbs:password" > ./bbs/dbauth
```

### 2. Install Libraries
```bash
$ pip install -r requirements.txt
```

### 3. Create Tables
```bash
$ python scripts/schema.py database
```

## RUN
```bash
$ python scripts/run.py
```

 ブラウザでhttp://localhost:5000 を開く

## DEVELOP
### サブパッケージの紹介
* modules リクエストを処理するコントローラーを置く
* models ORマッパーを置く
* scripts バッチスクリプトを置く
* service ビジネスロジックを置く
* lib 汎用ライブラリを置く
* templates テンプレートを置く

