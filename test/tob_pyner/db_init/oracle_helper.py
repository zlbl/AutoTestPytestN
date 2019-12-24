"""
Created on 2019年1月10日
@author: bobo

"""

import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class OracleHelper(object):
    """  oracle db operator  """

    def __init__(self, userName, password, host, port, instance):
        self._conn = cx_Oracle.connect(
            "%s/%s@%s:%s/%s" % (userName, password, host, port, instance))
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

    def get_table_metadata(self, table):
        self.cursor.execute("SELECT * FROM %s" % (table,))
        table_metadata = []
        # "The description is a list of 7-item tuples where each tuple
        # consists of a column name, column type, display size, internal size,
        # precision, scale and whether null is possible."
        for column in self.cursor.description:
            table_metadata.append({
                'name': column[0],
                'type': column[1],
                'display_size': column[2],
                'internal_size': column[3],
                'precision': column[4],
                'scale': column[5],
                'nullable': column[6],
            })
        return table_metadata

    # query methods
    def queryAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

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
        self.cursor.prepare(sql)
        self.cursor.executemany(None, nameParams)
        self.commit()

    def commit(self):
        self._conn.commit()

    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()

        if hasattr(self, '_conn'):
            self._conn.close()
