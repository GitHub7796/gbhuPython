import tomllib
from enum import Enum

# 定义环境枚举类
class ENV(Enum):
    SIT='sit'
    UAT='uat'
    PROD='pord'

# 定义读取 toml 的方法
def load_toml(toml_path):
    with open(toml_path,'rb') as fileObj:
        return tomllib.load(fileObj)