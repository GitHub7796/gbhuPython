import pymysql
from config.config_project import HOST, USER, PASSWORD, DATABASE


class DBhelpher(object):
    __coon = None
    __cursor = None

    def __init__(self):
        self.__coon = self.__getcoon()
        self.__cursor = self.__coon.cursor()

    def __getcoon(self):
        return pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )

    def fetch_many(self, sql, size):
        self.__cursor.execute(sql)
        return self.__cursor.fetchmany(size)
