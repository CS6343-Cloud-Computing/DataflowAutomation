from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.structs import TopicPartition
import os
import zmq
import threading
import time

kafkaServer = "192.168.1.82:9092"
producer = KafkaProducer(bootstrap_servers=kafkaServer,api_version=(0,11,5))

queue = []

def send_data():
    while(True):
        print(str("hi").encode("utf-8"))
        producer.send("firststep", value = str("hi-test").encode('utf-8'), partition=0, )
        producer.flush()
        # time.sleep(2)

def recv_header():
    while(True):
        msg = socket.recv()
        queue.append(msg)
        socket.send_string("200 Ok")
        print(queue)


if __name__ == "__main__":
    # listenerServer = threading.Thread(target=recv_header)
    produceData = threading.Thread(target=send_data())

    # listenerServer.start()
    produceData.start()

    # listenerServer.join()
    produceData.join()