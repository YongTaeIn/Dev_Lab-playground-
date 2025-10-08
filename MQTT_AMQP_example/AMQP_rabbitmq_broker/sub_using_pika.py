'''
    1. pika모듈을 이용한 통신
    2. AMQP(Advanced Message Queuing Protocol) 프로토콜 사용
'''

#!/usr/bin/env python
import pika, sys, os

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            virtual_host='/',
            credentials=pika.PlainCredentials('guest', 'guest')
        )
    )
    channel = connection.channel()


    # 1️⃣ Publisher와 같은 Exchange 선언
    channel.exchange_declare(exchange='logs', exchange_type='direct')


    # 2️⃣ Queue 선언
    channel.queue_declare(queue='info_queue')

    # 3️⃣ 같은 Binding 설정 (Exchange와 Queue를 연결)
    channel.queue_bind(exchange='logs', queue='info_queue', routing_key='info')


    # 4️⃣ 메시지 수신 함수
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}") # pika 모듈이 자동으로 인코딩해서 pub에서 보냈기때문에 decode 필요

    # 5️⃣ 해당 Queue를 구독 (consume)
    channel.basic_consume(queue='info_queue', on_message_callback=callback, auto_ack=True)


    #consuming start
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)