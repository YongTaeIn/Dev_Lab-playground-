# 🎓 Dev Lab Playground

> **Development archive for baseline testing and experiment records**

<div align="right">
  
[🇰🇷 한국어](./README.ko.md) | [🇺🇸 English](./README.md)

</div>

## 📌 프로젝트 목적

**실무 서비스 운용을 위한 핵심 개발 지식을 빠르게 습득하는 것**이 이 레포지토리의 목표입니다.

서비스를 안정적으로 운용하려면 서비스 특성에 맞는 개발 기술이 필요합니다. 이론만으로는 부족하고, 직접 실습하며 체득해야 실전에서 활용할 수 있습니다.

**이 레포지토리는:**
- ✅ 실무에서 자주 사용되는 기술을 선별
- ✅ 즉시 실행 가능한 예제 코드 제공
- ✅ 단계별 가이드로 빠른 학습 지원
- ✅ 실무 적용 사례를 통한 실전 감각 습득

---

## 📚 프로젝트 목록

### 1️⃣ [Kafka Example](./kafka_example)

**Apache Kafka 기초 입문**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Conda](https://img.shields.io/badge/Conda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://docs.conda.io/)

**🎯 학습 목표**  
Kafka Producer/Consumer 패턴 이해 및 메시지 큐 시스템 기본 구축

**📦 기술 스택**  
Kafka, Docker, Python, Conda

**💼 실무 사용 예시**
```
• 마이크로서비스 간 비동기 통신
  → 주문 서비스가 주문 정보를 Kafka에 전송 → 배송 서비스가 수신하여 처리

• 로그 수집 시스템
  → 여러 서버의 로그를 Kafka로 수집 → 중앙 로그 분석 서버에서 모니터링

• 이벤트 기반 아키텍처
  → 사용자 행동 이벤트(클릭, 구매)를 Kafka에 저장 → 추천 시스템, 분석 시스템이 활용
```

[📖 상세 가이드 보기](./kafka_example/readme.md)

---

### 2️⃣ [Kafka + Flink Example](./kafka_flink_example)

**실시간 스트림 데이터 처리**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![Flink](https://img.shields.io/badge/Apache%20Flink-E6526F?style=for-the-badge&logo=apache-flink&logoColor=white)](https://flink.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

**🎯 학습 목표**  
Kafka와 Flink를 결합한 실시간 데이터 파이프라인 구축 및 스트림 처리 이해

**📦 기술 스택**  
Kafka, Flink, Docker, Python

**💼 실무 사용 예시**
```
• 실시간 이상 탐지 시스템
  → IoT 센서 데이터를 Kafka로 수집 → Flink가 실시간 분석하여 이상값 감지 → 알림 발송

• 실시간 추천 시스템
  → 사용자 클릭스트림을 Kafka로 수집 → Flink가 실시간 분석 → 개인화된 추천 생성

• 금융 거래 모니터링
  → 거래 데이터를 Kafka로 수신 → Flink가 실시간으로 이상 거래 패턴 탐지 → 위험 거래 차단

• 실시간 대시보드
  → 서비스 메트릭을 Kafka로 수집 → Flink가 집계 및 계산 → 실시간 대시보드에 표시
```

[📖 상세 가이드 보기](./kafka_flink_example/readme.md)

---

### 3️⃣ [MQTT & AMQP Example](./MQTT_AMQP_example)

**메시지 큐 프로토콜 비교**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)](https://mqtt.org/)
[![Mosquitto](https://img.shields.io/badge/Mosquitto-3C5280?style=for-the-badge&logo=eclipsemosquitto&logoColor=white)](https://mosquitto.org/)
[![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://www.rabbitmq.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Conda](https://img.shields.io/badge/Conda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://docs.conda.io/)

**🎯 학습 목표**  
MQTT와 AMQP 프로토콜을 이해하고, 메시징 패턴을 비교하며, IoT와 엔터프라이즈 메시징 시스템 구현

**📦 기술 스택**  
MQTT (Paho + Mosquitto), AMQP (Pika + RabbitMQ), Docker, Conda

**💼 실제 사용 사례**
```
• IoT 센서 데이터 수집 (MQTT)
  → 온도 센서가 MQTT 브로커에 발행 → 모바일 앱이 구독하여 실시간 데이터 표시

• 스마트 홈 자동화 (MQTT)
  → 사용자가 앱으로 명령 전송 → MQTT 브로커 → 스마트 기기가 명령 실행

• 마이크로서비스 통신 (AMQP)
  → 주문 서비스 → RabbitMQ 큐 → 결제 서비스 → 배송 서비스 (전달 보장)

• 작업 큐 시스템 (AMQP)
  → 웹 서버가 백그라운드 작업 발행 → 워커 프로세스가 큐에서 소비하여 실행
```

[📖 상세 가이드 보기](./MQTT_AMQP_example/README.ko.md)

---

## 🚀 빠른 시작

### 설치 가이드

```bash
# 1. Repository 클론
git clone https://github.com/YongTaeIn/Dev_Lab-playground-.git
cd Dev_Lab-playground-

# 2. 원하는 프로젝트 선택
cd kafka_example  # or kafka_flink_example, MQTT_AMQP_example

# 3. README.md 확인하여 실행
cat readme.md
```

---

## 📖 각 프로젝트 상세 정보

### 🔧 기술 스택 비교

| 프로젝트 | Python | Kafka | Flink | MQTT | AMQP | Docker | Conda |
|---------|--------|-------|-------|------|------|--------|-------|
| **Kafka Example** | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Kafka + Flink** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| **MQTT & AMQP** | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |

---

## 🤝 기여하기

이 프로젝트는 학습 목적으로 만들어졌으며, 개선 제안이나 버그 리포트를 환영합니다!

```bash
# Issue 제기
https://github.com/YongTaeIn/Dev_Lab-playground-/issues

# Pull Request
https://github.com/YongTaeIn/Dev_Lab-playground-/pulls
```

---

## 📞 문의 및 피드백

- **GitHub Issues**: [이슈 등록하기](https://github.com/YongTaeIn/Dev_Lab-playground-/issues)
- **Email**: 필요시 이슈로 문의해주세요

---

## 📄 라이선스

이 프로젝트의 예제 코드는 학습 및 참고 목적으로 자유롭게 사용 가능합니다.

---

## 🌟 Star History

이 프로젝트가 도움이 되셨다면 ⭐ Star를 눌러주세요!

---

<div align="center">

**Happy Learning! 🎓**

*"실습을 통해 배우고, 경험을 통해 성장하세요."*

Made with ❤️ for learners

[⬆ 맨 위로 가기](#-dev-lab-playground)

</div>

