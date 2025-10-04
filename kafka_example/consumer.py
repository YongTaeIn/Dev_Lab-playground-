

from kafka import KafkaConsumer

# Kafka 컨슈머 생성
consumer = KafkaConsumer(
    'test-topic',
    group_id='test-group',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # 처음부터 읽기
    enable_auto_commit=True
)

print("Listening for messages...")
for message in consumer:
    print(f"{message.topic}:{message.partition}:{message.offset}: "
          f"key={message.key.decode('utf-8') if message.key else None}, "
          f"value={message.value.decode('utf-8')}")
