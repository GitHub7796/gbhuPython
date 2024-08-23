import pymysql
from config_project import HOST,USER,PASSWORD,DATABASE

# 获取数据库连接
def get_conn():
    return pymysql.connect(host=HOST,
                     user=USER,
                     password=PASSWORD,
                     database=DATABASE)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据。
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()