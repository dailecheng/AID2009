import pymysql

# 连接数据库
database = {"host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "stu",
            "charset": "utf8"}

db = pymysql.connect(**database)

# 生成游标
cur = db.cursor()
# 写操作示例 insert delete update
"""
# 若使用的引擎不支持事物,则execute()会直接提交
#(修改引擎alter table 表名 engine=innodb/myisam)
#不支持事物的引擎在同时写入多条数据时会倒序写入
name = input("请输入名字：")
# sql = f"update grade set 语文=50 where name='{name}'" #在能确认sql语句正确的情况下使用
# cur.execute(sql)
sql = "update grade set 语文=%s where name=%s"
cur.execute(sql,[50,name])# 此方法无需考虑数据类型
"""

# 支持事物的引擎默认会开启事物，需要用commit()提交修改
try:
    a = ("老爹", 0, 0, 0, 0)
    b = [("老爹", 0, 0, 0, 0),
         ("阿福", 1, 2, 3, 4),
         ("成龙", 5, 6, 7, 8),
         ("小玉", 100, 100, 100, 100)]
    sql = "insert into grade (name,语文,数学,英语,地理) values %s"
    # 自创写法,不推荐使用
    # 此语句不适用于cur.executemany() 故只能用for循环写入
    cur.execute(sql, [a])  # 传参容器里只有一个参数,即数组a,所以语句中对应的%s是一整个数组
    for row in b:
        print(row)
        cur.execute(sql, [row])  # for循环取到的数据再用[]打包一次,以对应sql语句中的一个%s--%s占位符

    sql = "insert into grade (name,语文,数学,英语,地理) values (%s,%s,%s,%s,%s)"
    cur.execute(sql, a)  # 传参容器用的是一个含有5个数据的元组,故sql语句中有5个%s
    # 相当于for循环,但是取到的数据无法再打包,故无法使用自创的写法
    cur.executemany(sql, b)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()
