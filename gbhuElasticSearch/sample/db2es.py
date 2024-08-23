from es_util import get_esconn
import sys
es_client=get_esconn()

# 从数据库获取数据 并 转化成 action
def get_actions():
    pass
# es 的逻辑，先删除索引、别名，然后添加索引、别名
def main():
    # 检验参数
    # 获取参数
    index=sys.args[1]
    # 获取对应数据
    actions=get_actions()
    
    # 查看索引是否存在
    es_client.indices.exists()
print(sys.args)