INDEX=""
INDEX_ALIAS=""
INDEX_BODY=""
datas=""
actions=[
    {
        "_index":INDEX,
        "_type":"_doc",
        "_id":data['id'],
        "_source":{k: v for k, v in data.items() if k != "id"}
    } for data in datas
]