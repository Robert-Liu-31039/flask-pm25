import pymysql
import pandas as pd


def open_db():
    conn = None
    try:
        conn = pymysql.connect(
            host="127.0.0.1", port=3306, user="root", passwd="12345678", db="demo"
        )
    except Exception as ex:
        print("資料庫開啟失敗", ex)

    return conn


def get_pm25_data_from_mysql():
    conn = None
    columns, datas = None, None

    try:
        conn = open_db()
        cursor = conn.cursor()

        sqlstr = "select * from pm25;"
        cursor.execute(sqlstr)

        # 取得 Table 的欄位名稱
        # print(cursor.description)
        columns = [col[0] for col in cursor.description]

        # 實際的資料
        datas = cursor.fetchall()
    except Exception as ex:
        print(ex)
    finally:
        if conn is not None:
            conn.close()

    return columns, datas


# 當程式是跑在本地運行的時候，才會跑以下的程式碼，
# 不然若是有其他程式 call 你這支程式碼時，
# 就會把以下的程式自動 run 起來了(誤跑)!
if __name__ == "__main__":
    datas = get_pm25_data_from_mysql()
    print(datas)
