import pymysql

# 创建数据库
#db = pymysql.connect(host="localhost",user='root',password='1234',port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

#创建表
# db = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

#插入数据库
id = '20120001'
user = 'Bob'
age = 20
data = {    
    'id': '20120002',
    'name': 'Bob',
    'age': 21
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
db = pymysql.connect(host='localhost',user='root',password='1234',port=3306,db='spiders')
cursor = db.cursor()
# sql = 'INSERT INTO students (id,name,age) VALUES(%s,%s,%s)'
sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table,keys = keys,values = values)
try:
    cursor.execute(sql,tuple(data.values()))
    print('success')
    db.commit()
except Exception as e:
    print('failed')
    print(e)
    db.rollback()
db.close()


