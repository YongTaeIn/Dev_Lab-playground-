'''
    1. pika모듈을 이용한 통신
    2. AMQP(Advanced Message Queuing Protocol) 프로토콜 사용
'''

'''
    [Simple] Producer -> Exchange -> Queue -> Consumer
    [Detail] Producer → [Exchange: logs] --(routing_key='info')--> [Queue: info_queue]

'''

#!/usr/bin/env python
import pika
 
#RabbitMQ 서버에 연결
#connection과 channel를 생성

connection = pika.BlockingConnection( # RabbitMQ 서버(브로커)에 실제로 TCP 연결을 생성하는 부분
    pika.ConnectionParameters( # RabbitMQ 서버에 어떻게 연결할지 속성 정의
        host='localhost', # RabbitMQ 서버 주소
        port=5672, # RabbitMQ 서버 포트
        virtual_host='/', # RabbitMQ 가상 호스트
        credentials=pika.PlainCredentials('guest', 'guest') # RabbitMQ 사용자 이름과 비밀번호
    )
)

# RabbitMQ 서버에서 채널을 생성하는 부분 
# 채널은 RabbitMQ 서버와 통신하는 일종의 가상 연결 통로
channel = connection.channel()

# 1️⃣ Exchange 선언 (메시지를 받아서 어떤 큐로 보낼지 결정하는 라우터 역할)
# 라우터린? : 메시지를 받아서 어떤 큐로 보낼지 결정
channel.exchange_declare(exchange='logs', exchange_type='direct')


# 2️⃣ Queue 선언 (메시지를 저장하는 공간)
channel.queue_declare(queue='info_queue')


# 3️⃣ Exchange와 Queue 연결 (Binding) (Exchange 와 Queue를 연결하고, 라우팅키를 지정)
# 의미 : 'logs' 익스체인지에서, routing_key='info'로 들어오는 메시지를, 'info_queue'로 전달하라는 의미.
channel.queue_bind(exchange='logs', queue='info_queue', routing_key='info')



# 4️⃣ 메시지 발행
channel.basic_publish(exchange='logs', routing_key='info', body='Hello, this is INFO message!')
print(" [x] Sent 'Hello, this is INFO message!'")

connection.close()

'''
    비유로 정리

    구성 요소	  비유	             역할
    Exchange	📮 “우체국”	       메시지를 받아서 어디로 보낼지 결정
    routing_key	📍 “주소”	       메시지를 어디(어떤 큐)로 가야 하는지 식별
    Queue	    📦 “우체통”	       메시지가 실제로 들어가 있는 저장소
    Binding	    📍 “주소 연결선”	Exchange가 어떤 메시지를 어느 Queue로 보낼지 규칙

'''