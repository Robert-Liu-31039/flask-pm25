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
    datas = None

    try:
        conn = open_db()
        cursor = conn.cursor()

        sqlstr = "select * from pm25;"
        cursor.execute(sqlstr)
        datas = cursor.fetchall()
    except Exception as ex:
        print(ex)
    finally:
        if conn is not None:
            conn.close()

    return datas
