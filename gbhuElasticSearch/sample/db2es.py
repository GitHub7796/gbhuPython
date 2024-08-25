import sys
import importlib
from loguru import logger
from helper.mysql_helper import DBhelpher
from config.config_project import PAGE_SIZE
from helper.es_helper import ESHealper
from decorators.log_decorators import log


@log()
def validate_arguments(args):
    pass


@log()
def import_index_moudle(argv):
    es_config_moudle = importlib.import_module('db2es.'+argv[0])

    return \
            es_config_moudle.INDEX_ALIAS, \
            es_config_moudle.INDEX_BODY, \
            es_config_moudle.SQL


def update_es_alias(index):
    pass


@log()
def db2es(index, sql):
    db_client = DBhelpher()
    es_client = ESHealper()
    while True:
        # 获取数据
        datas = db_client.fetch_many(sql, PAGE_SIZE)
        logger.success("fetch_many")
        if datas == ():
            break
        # 插入 es
        # es_client.insert_data(index,datas)
        break


def main(argv):
    # 检验参数
    validate_arguments(argv)
    # 动态导入模块
    INDEX_ALIAS, INDEX_BODY, SQL = import_index_moudle(argv)
    # 更新es
    db2es(INDEX_ALIAS, SQL)
    # 更新 alias
    update_es_alias(INDEX_ALIAS)


if __name__ == "__main__":
    main(sys.argv[1:])
