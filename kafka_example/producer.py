
from kafka import KafkaProducer

# Kafka 프로듀서 생성
producer = KafkaProducer(
    # 로컬에서 실행중인 브로커(브로커 이름 :localhost)의 9092(호스트 포트)에 연결하겠다.
    bootstrap_servers=['localhost:9092'], 
    key_serializer=lambda k: str(k).encode('utf-8'),
    value_serializer=lambda v: str(v).encode('utf-8')
)

# 메시지 전송
for i in range(10):
    producer.send('test-topic', key=f'key-{i}', value=f'hello {i}') # 토픽명 : test-topic
    print(f"Sent: key=key-{i}, value=hello {i}")

producer.flush()
producer.close()
