# 機器學習技法 final

## 開發規範

### 測資

由於官方提供的測資太大，不放進 git 管理，請各位自行下載放置於本專案的最高層目錄，亦即，目錄結構應該如下
```
.
├── data
│   ├── book_ratings_test.csv
│   ├── book_ratings_train.csv
│   ├── books.csv
│   ├── implicit_ratings.csv
│   ├── submission.csv
│   └── users.csv
├── Pipfile
├── Pipfile.lock
├── README.md
└── src
    └── util.py
```

### 使用 python3

統一使用 python3

### pipenv

python3 的 pip3 套件管理器預設會將函式庫安裝至整個系統，這可能可能發生以下情形：

甲裝了一個 A 庫，但乙沒裝，執行依賴於 A 庫的檔案時甲會成功，乙會報錯。

因此在協同開發時，會透過 pipenv 來同步彼此的環境（但它不是語言原生的，還是比 Node.js 的 npm 難用很多）。

pipenv 能讓開發者建立一個環境，使得 pip3 的安裝、移除都限制在這個環境之中，更多資訊可見[這篇教學](https://medium.com/@chihsuan/pipenv-%E6%9B%B4%E7%B0%A1%E5%96%AE-%E6%9B%B4%E5%BF%AB%E9%80%9F%E7%9A%84-python-%E5%A5%97%E4%BB%B6%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7-135a47e504f4)

請各位安裝、移除套件時，都透過 pipenv 來進行，以維持彼此套件同步。

## util 模組

src/util.py 中包含了數個能協助輸入輸出的函式，使用方法請直接去看檔案內的註解

