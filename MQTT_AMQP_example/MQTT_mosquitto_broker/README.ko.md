# MQTT Paho Example

> [English Version](./README.md) | 한국어

Paho-MQTT와 Mosquitto 브로커를 사용한 간단한 Pub/Sub 예제입니다.

## 🚀 빠른 시작

### 1. 환경 설정 및 브로커 시작
```bash
chmod +x setup.sh
./setup.sh
```

### 2. 터미널 1 - Subscriber 실행
```bash
conda activate mqtt_mosquitto_example
python sub_paho_example.py
```

### 3. 터미널 2 - Publisher 실행
```bash
conda activate mqtt_mosquitto_example
python pub_paho_example.py
```

### 4. 브로커 정지
```bash
docker-compose down
```

## 📁 파일 구조

- `environment.yml`: Conda 환경 정의
- `docker-compose.yml`: Mosquitto 브로커 설정
- `setup.sh`: 환경 설정 및 브로커 시작 스크립트
- `mosquitto.conf`: Mosquitto 설정 파일
- `pub_paho_example.py`: Publisher 코드
- `sub_paho_example.py`: Subscriber 코드

## 📡 포트 정보

- `1883`: MQTT 기본 포트
- `20518`: 테스트용 포트 (코드에서 사용)
- `9001`: WebSocket 포트 (선택사항)

## 🛠️ 문제 해결

### 브로커 로그 확인
```bash
docker-compose logs -f
```

### 브로커 상태 확인
```bash
docker ps | grep mqtt-broker
```

### 환경 재설정
```bash
conda env remove -n mqtt_mosquitto_example
./setup.sh
```
