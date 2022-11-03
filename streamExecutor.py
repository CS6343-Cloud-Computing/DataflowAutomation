from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.structs import TopicPartition
import os
import subprocess


class streamExecutor:
    def __init__(self):
        self.kafkaServer = "192.168.1.82:9092"
        self.consumeTopic = "firststep"
        self.kafka_init()

    def kafka_init(self):
        self.consumer = KafkaConsumer(
            bootstrap_servers=self.kafkaServer, api_version=(0, 11, 5), auto_offset_reset="earliest", group_id=None
        )
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafkaServer, api_version=(0, 11, 5))
        self.consumer.assign([TopicPartition(self.consumeTopic, 0)])

    def Exec(self):
        cmd = 'python3'
        for msg in self.consumer:
            data = msg.value
            userProcess = subprocess.Popen([cmd, '/home/m1-vm1/DataflowAutomation/ts.py',
                                           data], stdout=subprocess.PIPE, text=True, universal_newlines=True)
                                           
            output = str(userProcess.communicate()[0])
            print(msg)
            print(output, end='')


if __name__ == "__main__":
    se = streamExecutor()
    se.Exec()
