from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {"name": "kim", "age": 35}

res = es.index(index="test_index", body=doc)
print(res)

doc = {"sizes": 1, "query": {"term": {"DestiCityName": "Seoul"}}}
res = es.search(index="kibana_sample_Data_flights", body=doc)
print(res)
