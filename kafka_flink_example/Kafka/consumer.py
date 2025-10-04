from kafka import KafkaConsumer

# Kafka 컨슈머 생성
consumer = KafkaConsumer(
    'processed-topic', # 구독할 토픽명
    group_id='test-group',  # 컨슈머 그룹 ID
    # bootstrap_servers=['localhost:19092'], # kafka 클러스터에 접속을 위한 브로커 주소
    bootstrap_servers = ['127.0.0.1:19092'],
    auto_offset_reset='latest',  # 오프셋 초기화 전략
    enable_auto_commit=True # 자동 커밋 활성화
)

print("Listening for messages...")
for message in consumer:
    print(f"{message.topic}:{message.partition}:{message.offset}: "
          f"key={message.key.decode('utf-8') if message.key else None}, "
          f"value={message.value.decode('utf-8')}")



'''
    

    'kafka 클러스터' : 여러개의 브로커(서버)로 이루어진 집함.
        - 각 브로커는 고유한 ID와 주소 (host:port)를 가짐.
        - ex) booststra_server =['localhost:19092'] 

    ✓ group_id : 컨슈머 그룹 ID (컨슈머 그룹 내 컨슈머들은 동일한 그룹 ID를 가져야 함)

    ✓ bootstrap_servers : kafka 클러스터에 접속을 위한 브로커 주소

    ✓ auto_offset_reset : 오프셋 초기화 전략 (earliest: 처음부터, latest: 마지막부터, none: 오프셋 유지)
        - offset 이란? : 컨슈머가 읽은 메시지의 위치를 나타내는 값(index와 비슷)) (컨슈머가 읽은 메시지의 위치를 나타내는 값)

    ✓ enable_auto_commit : 자동 커밋 활성화 (True: 자동 커밋, False: 수동 커밋)

'''