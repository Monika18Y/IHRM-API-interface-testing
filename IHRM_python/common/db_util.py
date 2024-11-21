from pymysql import connect

class DBUtil(object):

    conn = None

    @classmethod
    def __get_conn(cls):
        if cls.conn is None:
            cls.conn = connect(
                host='localhost',
                port=3306,
                user='root',
                password='123456',
                database='test'
            )
        return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None

    # 常用方法：查询一条
    @classmethod
    def select_one(cls, sql):
        cursor = None
        res = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            print(f"查询结果为{res}")
        except Exception as err:
            print(f"查询sql错误：{err}")
        finally:
            cursor.close()
            cls.__close_conn()
            return res

    # 常用方法：增删改
    @classmethod
    def uid_db(cls, sql):
        cursor = None
        try:
            cls.conn = cls.__get_conn()
            cursor = cls.conn.cursor()
            cursor.execute(sql)
            print(f"影响的行数：{cls.conn.affected_rows()}")
            cls.conn.commit()
        except Exception as err:
            cls.conn.rollback()
            print(f"增删改sql错误：{err}，事务已回滚")
        finally:
            cursor.close()
            cls.__close_conn()


