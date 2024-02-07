import sys
from kafka import KafkaConsumer


def main(args):
  try:
    topic = args[0]
  except Exception as ex:
    print("Failed to set topic")

  consumer = get_kafka_consumer(topic)
  subscribe(consumer)


def subscribe(consumer_instance):
    try:
        for event in consumer_instance:
            key = event.key.decode("utf-8")
            value = event.value.decode("utf-8")
            print(f"Message Received: ({key}, {value})")
        consumer_instance.close()
    except Exception as ex:
        print('Exception in subscribing')
        print(str(ex))

def get_kafka_consumer(topic_name, servers=['localhost:1234']):
    _consumer = None
    try:
        _consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest', bootstrap_servers=servers, api_version=(0, 10), consumer_timeout_ms=10000)
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _consumer

if __name__ == "__main__":
  main(sys.argv[1:])