## INSTALL
python 練習用のWebアプリケーションテンプレートです。

### 1. Create Database Auth File
```bash
$ echo "user:database" > .myapp/dbauth
```

### 2. Install Libraries
```bash
$ pip -r requirements.txt
```

### 3. Create Tables
```bash
$ python scripts/schema.py database
```

## RUN
```bash
$ python scripts/run.py
```

## DEVELOP
### サブパッケージの紹介
* modules リクエストを処理するコントローラーを置く
* models ORマッパーを置く
* scripts バッチスクリプトを置く
* service ビジネスロジックを置く
* lib 汎用ライブラリを置く
* templates テンプレートを置く

