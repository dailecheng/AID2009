import pymysql

database = {"host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "stu",
            "charset": "utf8"}
# 连接数据库
db = pymysql.connect(**database)
# 生成游标
cur = db.cursor()
# 数据操作
try:
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()
