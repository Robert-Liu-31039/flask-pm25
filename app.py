from flask import Flask, render_template, request
from datetime import datetime
import pymysql
import pandas as pd

# __name__ <- 指的就是本頁
app = Flask(__name__)


# 宣告首頁的路徑
@app.route("/")
# 宣告立刻被執行的 function 方法
def index():
    # return f"<h1>Hello World!</h1><br>{datetime.now()}"
    books = {1: "Python book", 2: "Java book", 3: "Flask book"}
    for key in books:
        print(key, books[key])

    books_2 = [
        {
            "name": "Python book",
            "price": 299,
            "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
        },
        {
            "name": "Java book",
            "price": 399,
            "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
        },
        {
            "name": "C# book",
            "price": 499,
            "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
        },
    ]

    books_2 = []

    if books_2:
        for book in books_2:
            print(book["name"])
            print(book["price"])
            print(book["image_url"])
    else:
        print("販售完畢，目前無書籍!")

    username = "jerry"
    nowtime = datetime.now().strftime("%Y-%m-%d")
    print(username, nowtime)
    return render_template(
        "index.html", name=username, now=nowtime, books=books, books_2=books_2
    )


@app.route("/pm25-data")
def get_pm25_data():
    api_url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=540e2ca4-41e1-4186-8497-fdd67024ac44&limit=1000&sort=datacreationdate%20desc&format=CSV"
    datas = pd.read_csv(api_url, encoding="utf-8-sig")
    datas["datacreationdate"] = pd.to_datetime(datas["datacreationdate"])
    df = datas.drop(datas[datas["pm25"].isna()].index)
    return df.values.tolist()


@app.route("/bmi")
def get_bmi():
    # request.args.get("@參數名稱) -> 根據 form 所回傳的參數內容，去做參數的值的接取
    height = eval(request.args.get("height"))
    weight = eval(request.args.get("weight"))

    bmi = round(weight / (height / 100) ** 2, 2)
    return {"height": height, "weight": weight, "bmi": bmi}


# 讓 Flask Server run 起來
app.run(debug=True)
