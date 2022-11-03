from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.structs import TopicPartition
import os
import zmq
import threading
import json
from collections import defaultdict
lock = threading.Lock()
import time

class streamStartStub:
    def __init__(self):
        self.subToPort = defaultdict(set)
        self.portToPub = defaultdict()
        self.zeromq_init()
        self.kafka_consumer_init()

        listenerServer = threading.Thread(target=self.server_thread)
        listenerServer.start()

        publishData = threading.Thread(target=self.publisher_thread)
        publishData.start()

        listenerServer.join()
        publishData.join()

    def zeromq_init(self):
        self.context = zmq.Context()
        self.zeromqServer = self.context.socket(zmq.REP)
        self.zeromqServer.bind("tcp://*:5555")


    def kafka_consumer_init(self):
        self.kafkaServer = "192.168.1.82:9092"
        self.consumer = KafkaConsumer(
            bootstrap_servers=self.kafkaServer, api_version=(0, 11, 5), auto_offset_reset="earliest", group_id=None
        )

    def server_thread(self):
        while(True):
            msg = self.zeromqServer.recv_json()
            action = msg["Action"]
            topic = msg["Topic"]
            port = msg["Port"]

            
            if(action == "Sub"):
                if port not in self.portToPub:
                    pubSocket = self.context.socket(zmq.PUB)
                    pubSocket.bind("tcp://*:%s" % port)
                    self.portToPub[port] = pubSocket
                self.subToPort[topic].add(port)
            elif(action == "Unsub"):
                if port in self.portToPub:
                    self.portToPub[port].close()
                    del self.portToPub[port]
                if port in self.subToPort[topic]:
                    self.subToPort[topic].remove(port)
                if len(self.subToPort[topic]) == 0:
                    del self.subToPort[topic]
            
            # print(self.subToPort)
            # print(self.portToPub)
            
            topicsList = list(self.subToPort.keys())
            #self.consumer.unsubscribe()
            print(topicsList)
            topicPartitions = [TopicPartition(topic, 0) for topic in topicsList]
            print(topicPartitions)
            if len(topicsList) > 0:
                self.consumer.assign(topicPartitions)
                # self.consumer.subscribe(topics=topicsList)
            else:
                print("here")
                self.consumer.assign([TopicPartition("dummy", 0)])
            self.zeromqServer.send_json({"Result":"200 ok"})

    def publisher_thread(self):
        for msg in self.consumer:
            print(msg)

if __name__ == "__main__":
    ss = streamStartStub()



    
    
