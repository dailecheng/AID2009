import re

l = []
with open("dict.txt") as file:
    for line in file:
        # info = re.findall(r"(\w+)\s+(.*)", line)
        # print(info)
        # l+=info
        tmp = line.split(" ", 1)
        info = (tmp[0], tmp[1].strip())
        print(info)
        l.append(info)
import pymysql

database = {"host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "dict",
            "charset": "utf8"}
# 连接数据库
db = pymysql.connect(**database)
# 生成游标
cur = db.cursor()
# 数据操作
try:
    sql = "insert into words (word,mean) values (%s,%s)"
    cur.executemany(sql, l)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()

# ['zoology          n. scientific study of the structure, form and distribution of animals']
# ['zygote           the cell resulting from the union of an ovum and a spermatozoon']
# ['zoology          n. scientific study of the structure, form and distribution of animals']
# ['zygote           the cell resulting from the union of an ovum and a spermatozoon']
