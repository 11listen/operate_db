#coding: utf-8

import MySQLdb

#connect db
db = MySQLdb.connect("192.168.0.107", "admin_zone", "xxxxxx", "detection")

#get vernier
cursor = db.cursor()

#sql statement
db_sql = """
        CREATE TABLE iptable (
        user char(20) not null,
        job char(20) not null,
        mac char(48) not null,
        ip char(64) not null,
        description char(128)
        )
        """
#execute sql
data = cursor.execute( """
show tables like 'iptable'
""")

#if db not exists, create db, else, insert sql statement
try:
    if data == 0:
        cursor.execute(db_sql)
        print "db is create"
except:
        print "db is exist, the data will insert db"

#dynamically inserted into the datebase
def operate(operation):
    operate_json = operation
    for data_json in operate_json.items():
        data_list = data_json[1]
        get_list = eval(data_list)
        for y in get_list:
            for get_tuple in y.items():
                value = get_tuple[1]
                sql = """INSERT INTO iptable VALUES (%(user)s, %(job)s, %(mac)s, %(ip)s, %(description)s)"""
                try:
                    cursor.execute(sql, value)
                    db.commit()
                    print 'success json has been insert db'
                except:
                    db.rollback()
                    print 'error, please check your operat'
