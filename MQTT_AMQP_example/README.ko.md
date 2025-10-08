# 🔌 MQTT & AMQP Examples

> [English](./README.md) | 한국어

MQTT와 AMQP 프로토콜을 비교하고 실용적인 예제를 제공하는 종합 가이드입니다.

## 📌 무엇이 다를까?

### MQTT vs AMQP 개요

| 측면 | MQTT | AMQP |
|------|------|------|
| **전체 이름** | Message Queuing Telemetry Transport | Advanced Message Queuing Protocol |
| **설계 목표** | 경량 IoT 메시징 | 엔터프라이즈 메시지 큐잉 |
| **프로토콜 유형** | Topic 기반 Pub/Sub | Queue 기반 메시징 |
| **오버헤드** | 매우 낮음 (~2바이트 헤더) | 높음 (~8바이트 헤더) |
| **QoS 레벨** | 3단계 (0, 1, 2) | 다중 전달 보장 |
| **최적 사용처** | IoT, 모바일, 센서 | 마이크로서비스, 엔터프라이즈 |
| **대역폭** | 저대역폭 최적화 | 일반/고대역폭 |
| **복잡도** | 단순 | 복잡 |
| **라우팅** | Topic 와일드카드 | 복잡한 Exchange 라우팅 |

---

## 🔍 상세 비교

### 1️⃣ **아키텍처 패턴**

#### MQTT (Topic 기반 Pub/Sub)
```
Publisher → [Topic: sensor/temperature] → Broker → Subscribers
                                           ↓
                                    관심있는 모든 클라이언트
```
- Publisher가 **topic**에 발행
- Subscriber가 **topic 패턴** 구독
- 직접적인 큐 개념 없음
- 다대다 통신

#### AMQP (Queue 기반 메시징)
```
Producer → [Exchange] → [Binding Rules] → [Queue] → Consumer
                ↓
          라우팅 로직
```
- Producer가 **exchange**에 전송
- 메시지가 binding을 통해 **queue**로 라우팅
- Consumer가 특정 큐에서 읽음
- 점대점 또는 팬아웃 패턴

---

### 2️⃣ **메시지 전달 보장**

#### MQTT QoS 레벨
```
QoS 0: 최대 1회  (발행 후 잊기)
  → 응답 없음, 가장 빠름, 손실 가능

QoS 1: 최소 1회 (응답 전달)
  → 전달 보장, 중복 가능

QoS 2: 정확히 1회  (4-way handshake)
  → 정확히 한 번 보장, 가장 느림, 중복 없음
```

#### AMQP 보장
```
- 응답 확인 (수동/자동)
- 트랜잭션 지원
- Publisher 확인
- 영속 메시지 (브로커 재시작 후에도 유지)
- Dead letter 큐 (실패한 메시지)
```

---

### 3️⃣ **사용 사례**

#### ✅ MQTT를 사용할 때:
- IoT 센서 네트워크 구축
- 모바일 앱 푸시 알림
- 실시간 위치 추적
- 저대역폭/불안정한 네트워크
- 배터리 구동 장치
- 단순 pub/sub 필요

**예시:**
```
스마트 홈: 온도 센서 → MQTT 브로커 → 모바일 앱
```

#### ✅ AMQP를 사용할 때:
- 마이크로서비스 통신
- 작업 큐 시스템
- 금융 거래
- 주문 처리 파이프라인
- 전달 보장 필요
- 복잡한 라우팅 필요

**예시:**
```
이커머스: 주문 서비스 → RabbitMQ → 결제 서비스 → 배송 서비스
```

---

### 4️⃣ **프로토콜 오버헤드**

#### MQTT
```python
# 최소한의 패킷 구조
Fixed Header: 2바이트
Variable Header: 최소
Payload: 실제 데이터

총 오버헤드: ~2-4바이트
```

#### AMQP
```python
# 더 구조화된 패킷
Frame Header: 8바이트
Protocol Header: 추가 바이트
Content properties: 메타데이터

총 오버헤드: ~8-12바이트
```

**영향:** MQTT는 작은 메시지에 대해 2-3배 가벼움

---

### 5️⃣ **Topic vs Queue 라우팅**

#### MQTT Topics (계층적)
```
sensor/living-room/temperature
sensor/bedroom/temperature
sensor/+/temperature          # 단일 레벨 와일드카드
sensor/#                      # 다중 레벨 와일드카드
```

#### AMQP Exchanges & 라우팅
```
Direct Exchange:    정확한 라우팅 키 매칭
Fanout Exchange:    모든 큐에 브로드캐스트
Topic Exchange:     패턴 매칭 (*, #)
Headers Exchange:   헤더 기반 라우팅
```

---

## 📚 이 리포지토리의 예제

### 1️⃣ Paho MQTT 예제 (Mosquitto 브로커)

**프로토콜:** MQTT  
**클라이언트:** Paho-MQTT  
**브로커:** Mosquitto  

📖 [예제 보기](./paho_example(mosquitto)/)

---

### 2️⃣ Pika AMQP 예제 (RabbitMQ 브로커)

**프로토콜:** AMQP  
**클라이언트:** Pika  
**브로커:** RabbitMQ  

📖 [예제 보기](./pika_example(rabbitmq)/)

---

## 🎯 어떤 것을 선택해야 할까?

### MQTT를 선택하세요:
- ✅ 경량 프로토콜
- ✅ 낮은 전력 소비
- ✅ 모바일/IoT 장치
- ✅ 단순 pub/sub
- ✅ 불안정한 네트워크
- ✅ 저대역폭

### AMQP를 선택하세요:
- ✅ 전달 보장
- ✅ 복잡한 라우팅
- ✅ 엔터프라이즈 기능
- ✅ 트랜잭션 지원
- ✅ 마이크로서비스
- ✅ 높은 신뢰성

---

## 🔧 성능 비교

| 지표 | MQTT | AMQP |
|------|------|------|
| **처리량** | 높음 (가벼움) | 낮음 (오버헤드 많음) |
| **지연시간** | 낮음 (~1-5ms) | 높음 (~5-15ms) |
| **CPU 사용량** | 낮음 | 높음 |
| **메모리** | 낮음 | 높음 |
| **확장성** | 많은 클라이언트에 우수 | 많은 큐에 우수 |

---

## 🌐 실제 사용 예시

### MQTT 실전 활용
```
🏠 스마트 홈
  - 온도 조절기 발행: home/temperature
  - 앱 구독: home/#
  - 전구 구독: home/lights/+

📱 모바일 채팅
  - 사용자 메시지 전송: chat/room123
  - 모든 방 멤버 구독: chat/room123

🚗 차량 추적
  - 차량 발행: fleet/vehicle/{id}/location
  - 관제센터 구독: fleet/vehicle/+/location
```

### AMQP 실전 활용
```
🛒 이커머스 주문 처리
  1. 주문 서비스 → order.placed 큐
  2. 결제 서비스가 order.placed에서 소비
  3. 결제 서비스 → order.paid 큐
  4. 배송 서비스가 order.paid에서 소비

📧 이메일 서비스
  - 웹 앱 → email.send 큐
  - 워커 프로세스가 소비하여 이메일 전송
  - 실패한 이메일 → dead letter 큐

🔄 마이크로서비스
  - API Gateway → 다중 서비스 큐
  - 각 서비스가 전용 큐 보유
  - 워커 간 로드 밸런싱
```

---

## 🚀 빠른 시작

### 리포지토리 클론
```bash
git clone https://github.com/YongTaeIn/Dev_Lab-playground-.git
cd Dev_Lab-playground-/MQTT_AMQP_example
```

### MQTT 예제 실행
```bash
cd paho_example(mosquitto)
chmod +x setup.sh
./setup.sh
```

### AMQP 예제 실행
```bash
cd pika_example(rabbitmq)
chmod +x setup.sh
./setup.sh
```

---

## 📖 더 알아보기

### MQTT 리소스
- [MQTT 공식](https://mqtt.org/)
- [Eclipse Paho](https://eclipse.org/paho/)
- [Mosquitto 브로커](https://mosquitto.org/)

### AMQP 리소스
- [AMQP 명세](https://www.amqp.org/)
- [RabbitMQ 공식](https://www.rabbitmq.com/)
- [Pika 문서](https://pika.readthedocs.io/)

---

## 🤝 기여

기여를 환영합니다! 이슈나 풀 리퀘스트를 제출해주세요.

---

**즐거운 메시징! 📨**

_"필요에 따라 다른 프로토콜을 - 현명하게 선택하세요!"_
