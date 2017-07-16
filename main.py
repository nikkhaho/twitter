import threading,time
from kafka import KafkaConsumer, KafkaProducer
import get_data_from_twitter
import json
import elastic_search
import datetime
import get_from_text
import requests



class Consumer(threading.Thread):
    def run(self):

      while 1:
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
        consumer.subscribe(['q1'])

        for message in consumer:

            hashtag=message.value.decode("utf-8")
            tweets=get_data_from_twitter.gettwbytag(hashtag)
            print(tweets)
            print("tag")

            for twjson in tweets:
              # print(twjson)
              tweetid=(twjson['tweetid'])
              elastic=elastic_search.save_to_elastic(twjson,tweetid)
              listhash=(twjson['hashtags'])
              list_id=(twjson['ids'])
              producer = KafkaProducer(bootstrap_servers='192.168.43.50:9092')
              for hashtags in listhash:
                producer.send('q1',hashtags.encode("utf-8"))
                # print(hashtags)
              for ids in list_id:
                producer.send('qid',ids.encode("utf-8"))
              #   print(ids)
                # print(listhash)
            # time.sleep(300)
# ///////////////////////////end consumer/////////////////////////////////////////
class Producer(threading.Thread):
     def run(self):


      while 1:
        consumer1 = KafkaConsumer(bootstrap_servers='localhost:9092')
        consumer1.subscribe(['q2'])

        for message1 in consumer1:

            ids=message1.value.decode("utf-8")
            text=get_from_text.get_idd(ids)
            tweets1=get_data_from_twitter.gettwbyid(text)
            # print(tweets1)
            for twjson1 in tweets1:
              # print(twjson1)
              tweetid1=(twjson1['tweetid'])
              elastic=elastic_search.save_to_elastic(twjson1,tweetid1)
              listhash1=(twjson1['hashtags'])
              list_id1=(twjson1['ids'])
              producer = KafkaProducer(bootstrap_servers='192.168.43.50:9092')
              for hashtags in listhash1:
                producer.send('q1',hashtags.encode("utf-8"))
                # print(hashtags)
              for ids in list_id1:
                producer.send('qid',ids.encode("utf-8"))
                # print(ids)
                # print(listhash)
            # time.sleep(300)
# ///////////////////////////////////////////////////////////////
def main():
    threads = [
        Consumer(),
        Producer()
    ]
    for t in threads:
        t.start()
if __name__ == "__main__":

    main()