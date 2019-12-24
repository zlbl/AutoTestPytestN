# -*- coding:utf-8 -*-
import pymysql

"""
数据库操作类
"""


class DbUtil:
    dbconnect = None;
    hostname = '';
    password = '';
    dbname = '';
    port = '';

    def __init__(self, hostname, username, password, dbname, port):
        self.hostname = hostname;
        self.username = username;
        self.password = password;
        self.dbname = dbname;
        self.port = port

    """
    获取mysql连接对象
    """
    def open_connect(self):
        try:
            # 创建数据库连接
            self.dbconnect = pymysql.connect(host=self.hostname, user=self.username, passwd=self.password, db=self.dbname, port=self.port, charset='utf8');
        except:
            print('打开连接异常')

    """
    数据添加操作
    """
    def insert_data(self,sql):
        # 使用cursor()方法获取操作游标
        cursor = self.dbconnect.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql);
            # 提交到数据库执行
            self.dbconnect.commit();
            last_id = self.get_last_insert_id(cursor);
            cursor.close();
            return last_id;
        except:
            # 如果发生错误则回滚
            self.dbconnect.rollback();
            print('请检查sql语法是否正确');
            return 0;

    """
    获取数据添加成功后的自增ID
    """
    def get_last_insert_id(self,cursor):
        sql = 'SELECT LAST_INSERT_ID() AS id;';
        cursor.execute(sql);
        database = cursor.fetchone();
        return database[0];

    """
    查询单条数据
    """
    def find_one(self, sql):
        # 使用cursor()方法获取操作游标
        cursor = self.dbconnect.cursor();
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchone()
            cursor.close();
            return results;
        except:
            print("Error: unable to fetch data")
            return None;

    """
    关闭数据库连接
    """
    def close_connect(self):
        if self.dbconnect is not None:
            self.dbconnect.close();