#!/usr/bin/env python
# coding: utf-8
import pymysql
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("DbBase")


# 初始化数据库
class DbBase(object):
    def __init__(self, host, port, user, passwd, db, charset):
        try:
            self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset)
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            logging.error("连接数据库出错，原因：%s" % e)

    def __del__(self):
        self.conn.close()
        self.cur.close()

    # 查询操作,看是否有条件
    def query(self, sql, data=None):
        try:
            if not data:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, data)
            results = self.cur.fetchall()
            return results
        except Exception as e:
            logging.error("查询失败，原因：%s" % e)

    def insert(self, sql, data):
        try:
            self.cur.execute(sql, data)
            self.conn.commit()
            logging.info("DbBase.insert_data -- 插入数据成功！")
        except Exception as e:
            self.conn.rollback()
            logging.error("数据库插入数据出错，原因：%s,数据%s" % (e, data))

    def insertRows(self, sql, data):
        try:
            self.cur.executemany(sql, data)
            self.conn.commit()
            logging.info("DbBase.insert_data -- 插入数据成功！")
        except Exception as e:
            self.conn.rollback()
            logging.error("数据库插入数据出错，原因：%s,数据%s" % (e, data))

    def delete(self, sql, data=None):
        try:
            if not data:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, data)
                self.conn.commit()
            logging.info("DbBase.insert_data -- 插入数据成功！")
        except Exception as e:
            self.conn.rollback()
            logging.error("数据库删除数据出错，原因：%s,数据%s" % (e, data))

    def update(self, sql, data=None):
        try:
            if not data:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, data)
                self.conn.commit()
            logging.info("DbBase.insert_data -- 插入数据成功！")
        except Exception as e:
            self.conn.rollback()
            logging.error("数据库更新数据出错，原因：%s,数据%s" % (e, data))
