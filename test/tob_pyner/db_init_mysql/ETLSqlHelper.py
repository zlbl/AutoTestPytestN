import pymysql
from DBUtils.PooledDB import PooledDB, SharedDBConnection

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=100,  # 连接池允许的最大连接数，0和None表示没有限制
    mincached=100,  # 初始化时，连接池至少创建的空闲的连接，0表示不创建
    maxcached=100,  # 连接池空闲的最多连接数，0和None表示没有限制
    maxshared=3,
    # 连接池中最多共享的连接数量，0和None表示全部共享，ps:其实并没有什么用，因为pymsql和MySQLDB等模块中的threadsafety都为1，所有值无论设置多少，_maxcahed永远为0，所以永远是所有链接共享
    blocking=True,  # 链接池中如果没有可用共享连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
    setsession=[],  # 开始会话前执行的命令列表
    ping=0,  # ping Mysql 服务端，检查服务是否可用
    host='192.168.5.94',
    port=3306,
    user='root',
    password='123456',
    # database='b2b_pyner_depository_bobo_test',
    database='b2b_pyner_itf_bobo_test',
    # database='b2b_pyner_depository_mie',
    charset='utf8'
)


def insert_batch(sql, params=[]):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.executemany(sql, params)
    commit(conn)


def commit(conn):
    conn.commit()
    # 这里close不是真的close了，是还回去了
    conn.close()


# 查询所有字段
def list_col(table_name):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("select * from %s" % table_name)
    col_name_list = [tuple[0] for tuple in cursor.description]
    return col_name_list


def list_table():
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("show tables")
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    return table_list
