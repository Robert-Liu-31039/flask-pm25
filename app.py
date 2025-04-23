from flask import Flask, render_template
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
    username = "jerry"
    nowtime = datetime.now().strftime("%Y-%m-%d")
    print(username, nowtime)
    return render_template("index.html", name=username, now=nowtime)


@app.route("/pm25_data")
def get_pm25_data():
    api_url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=540e2ca4-41e1-4186-8497-fdd67024ac44&limit=1000&sort=datacreationdate%20desc&format=CSV"
    datas = pd.read_csv(api_url, encoding="utf-8-sig")
    datas["datacreationdate"] = pd.to_datetime(datas["datacreationdate"])
    df = datas.drop(datas[datas["pm25"].isna()].index)
    return df.values.tolist()


# 讓 Flask Server run 起來
app.run(debug=True)
