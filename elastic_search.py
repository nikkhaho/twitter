from elasticsearch import Elasticsearch
import requests
def save_to_elastic(twjson,tweetid):
 a=[]
 es = Elasticsearch(hosts="127.0.0.1",port='9200')
 es.index(
     index="test",
     doc_type="tb_test1",
     id=tweetid,
     body=twjson
 )

