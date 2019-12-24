"""
Created on 2019年1月10日
@author: bobo

"""

import pymysql


class MySQLHelper(object):
    """  mysql db operator  """

    def __init__(self, user_name, password, host, port, database):
        self._conn = pymysql.connect(
            host=host,
            user=user_name,
            password=password,
            database=database,
            charset='utf8')
        self.cursor = self._conn.cursor()

    def queryTitle(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        colNames = []
        for i in range(0, len(self.cursor.description)):
            colNames.append(self.cursor.description[i][0])

        return colNames

    # query methods
    def queryAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # query methods
    def queryMany(self, sql, num):
        self.cursor.execute(sql)
        return self.cursor.fetchmany(self.cursor, num)

    def queryOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def queryBy(self, sql, nameParams={}):
        if len(nameParams) > 0:
            self.cursor.execute(sql, nameParams)
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()

    def insertBatch(self, sql, nameParams=[]):
        """batch insert much rows one time,use location parameter"""
        self.cursor.executemany(sql, nameParams)
        self.commit()

    def execute(self, sql):
        """batch insert much rows one time,use location parameter"""
        self.cursor.execute(sql)
        self.commit()

    def commit(self):
        self._conn.commit()

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()

        if hasattr(self, '_conn'):
            self._conn.close()
