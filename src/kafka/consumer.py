from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:1234')

for msg in consumer:
	print(msg)