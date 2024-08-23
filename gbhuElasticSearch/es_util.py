from elasticsearch import Elasticsearch
from config_util import load_toml

config=load_toml('gbhuElasticSearch/config.toml')
IP=config['elasticSearch']['ip']
PORT=config['elasticSearch']['port']

def get_esconn():
    return Elasticsearch([{"host":IP,"port":PORT}])