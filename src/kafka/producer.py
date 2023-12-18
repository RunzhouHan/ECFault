from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:1234')

while True:
	producer.send("iostat","read=0MB/s, write=0MB/s")
