from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.structs import TopicPartition
from textblob import TextBlob
import os


class InOut:
    def __init__():
        self.kafkaServer = os.environ.get('KafkaServer')
        self.containerName = os.environ.get('ContainerName')
        self.consumer = KafkaConsumer(
            bootstrap_servers=kafkaServer, api_version=(0,11,5), auto_offset_reset='earliest', group_id=None
        )
        self.consumer.subscribe(topics=containerName)
        self.producer = KafkaProducer(bootstrap_servers=kafkaServer,api_version=(0,11,5))

    def Read():
        return self.consumer

    def Write(data: string) -> None:
        self.producer.send("output", value=data)