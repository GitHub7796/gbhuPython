from elasticsearch import Elasticsearch
from gbhuElasticSearch.sample.config_project import CONN_CONFIG

def get_esconn():
    return Elasticsearch(CONN_CONFIG)