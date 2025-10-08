# RabbitMQ Pika Example

> [English Version](./README.md) | 한국어

Docker를 사용한 Pika (RabbitMQ Python 클라이언트) Pub/Sub 예제입니다.

## 🚀 빠른 시작

### 1. 환경 설정 및 브로커 시작
```bash
chmod +x setup.sh
./setup.sh
```

### 2. 터미널 1 - Subscriber 실행
```bash
conda activate rabbitmq_pika_example
python sub_using_pika.py
```

### 3. 터미널 2 - Publisher 실행
```bash
conda activate rabbitmq_pika_example
python pub_using_pika.py
```

### 4. 브로커 정지
```bash
docker-compose down
```

## 📁 파일 구조

- `environment.yml`: Conda 환경 정의
- `docker-compose.yml`: RabbitMQ 브로커 설정
- `setup.sh`: 환경 설정 및 브로커 시작 스크립트
- `pub_using_pika.py`: Publisher 코드
- `sub_using_pika.py`: Subscriber 코드

## 📡 포트 정보

- `5672`: RabbitMQ AMQP 포트
- `15672`: RabbitMQ 관리 UI
  - URL: http://localhost:15672
  - 사용자명: `guest`
  - 비밀번호: `guest`
- `20518`: 대체 포트 매핑

## 🔧 설정

필요시 Python 파일에서 연결 파라미터를 수정하세요:
```python
pika.ConnectionParameters(
    'localhost',  # RabbitMQ 서버 주소
    5672,         # 포트
    '/',          # Virtual host
    pika.PlainCredentials('guest', 'guest')  # 사용자명/비밀번호
)
```

## 🛠️ 문제 해결

### 브로커 로그 확인
```bash
docker-compose logs -f rabbitmq
```

### 브로커 상태 확인
```bash
docker ps | grep rabbitmq-broker
```

### 관리 UI 접속
브라우저에서 http://localhost:15672 열기
- 기본 계정: guest/guest
- 큐, 교환기, 메시지 확인 가능

### 환경 재설정
```bash
conda env remove -n rabbitmq_pika_example
docker-compose down -v  # 볼륨 삭제
./setup.sh
```

## 📝 참고사항

- Pika는 순수 Python RabbitMQ 클라이언트 라이브러리입니다
- RabbitMQ는 AMQP 프로토콜 사용 (Advanced Message Queuing Protocol)
- 보장된 전달을 제공하는 큐 기반 메시징
- 클러스터링 지원하는 엔터프라이즈급 메시지 브로커
- `setup.sh` 스크립트가 모든 설정을 자동으로 처리합니다
- `setup.sh` 실행 전 Docker가 실행 중이어야 합니다

## 🆚 AMQP vs MQTT

| 특징 | AMQP (RabbitMQ) | MQTT (Mosquitto) |
|------|-----------------|------------------|
| **프로토콜** | AMQP | MQTT |
| **메시징** | Queue 기반 | Topic 기반 |
| **안정성** | 보장된 전달 | QoS 레벨 (0,1,2) |
| **사용 사례** | 엔터프라이즈, 마이크로서비스 | IoT, 모바일 |
| **오버헤드** | 높음 | 낮음 |
| **복잡도** | 복잡한 라우팅 | 단순 Pub/Sub |
