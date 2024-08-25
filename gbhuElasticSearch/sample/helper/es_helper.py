from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from config.config_project import CONN_CONFIG

class ESHealper():
    __es_client=None
    def __init__(self) -> None:
        self.__es_client=Elasticsearch(CONN_CONFIG)
    def insert_data(self,index,datas):
        print(datas)
        actions = [
            {
                "_index": index,
                "_type": "_doc",
                # "_id": data['id'],
                # "_source": {k: v for k, v in data.items() if k != "id"}
                "_source": data
            } for data in datas
        ]
        bulk(self.__es_client, actions)