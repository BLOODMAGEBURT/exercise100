# -*- coding: utf-8 -*-
# 导入mysql 驱动
import mysql.connector


conn = mysql.connector.connect(host='192.168.1.253', user='root', password='123456', database='test', port=3306)
cursor = conn.cursor()

# 创建表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入记录
# cursor.execute('insert into roles(id, name ) values(%s, %s)', ['2', 'mike'])
# cursor.execute('insert into user(id, name ) values(%s, %s)', ['3', 'jojo'])

# 查询记录
# cursor.execute('select * from roles where roleId = %s', ('3',))

# results = cursor.fetchall()


# print results
#
#
# names = [x[0] for x in cursor.description]
#
# print names, 'type:', type(names)
#
#
# print 'description:', cursor.description
# print 'results:', results
# print 'count:', cursor.rowcount
# 提交事务
conn.commit()

# 关闭连接
cursor.close()
conn.close()



