import csv
import subprocess
from kafka import KafkaProducer


def main(args):
  try:
    topic = args[0]
    key = args[1]
    message = args[2]
  except Exception as ex:
    print("Failed to set topic, key, or message")

  producer = get_kafka_producer()
  publish(producer, topic, key, message)


def publish(producer_instance, topic_name, key, value, loops):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print(f"Publish Succesful ({key}, {value}) -> {topic_name}")
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))

def get_kafka_producer(servers=['localhost:9092']):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=servers, api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

def iostat():
	io_c = subprocess.Popen(['iostat', '-xnsMr', '1', '2'], stdout=subprocess.PIPE, shell=False, stderr=subprocess.PIPE)
	stdout = io_c.communicate()[0]

if __name__ == "__main__":
  main(sys.argv[1:])