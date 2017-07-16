#!/usr/bin/env python



import db
import savetag
import saveid



import threading, logging, time

from kafka import KafkaConsumer, KafkaProducer


class Producer_tag(threading.Thread):
    # daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')

        while True:

            d=db.getfromtb("tb_tag")
            for g in d:
              producer.send('q1',str(g).encode('utf-8'))

            time.sleep(2)

class Producer_id(threading.Thread):
    # daemon = True

    def run(self):
        producer2 = KafkaProducer(bootstrap_servers='localhost:9092')
        while True:
            t=db.getfromtb("tb_id")
            for p in t:
              producer2.send('q2',str(p).encode('utf-8'))
            time.sleep(2)


class Consumer_tag(threading.Thread):
    # daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092')

        consumer.subscribe(['q1'])

        for message in consumer:
             o=message.value.decode('utf-8')
             savetag.save1(o)

             # print(o)

class Consumer_id(threading.Thread):
    # daemon = True

    def run(self):
        consumer2 = KafkaConsumer(bootstrap_servers='localhost:9092')

        consumer2.subscribe(['qid'])

        for message in consumer2:
             o=message.value.decode('utf-8')
             saveid.save1(o)


             # print(o)




def main():
    threads = [
         Producer_tag(),
         Consumer_tag(),
          Consumer_id(),
        Producer_id()
    ]

    for t in threads:
        t.start()

    # time.sleep(10)

if __name__ == "__main__":

    main()
