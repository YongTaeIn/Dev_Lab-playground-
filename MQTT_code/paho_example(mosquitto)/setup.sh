#!/bin/bash

# MQTT Mosquitto Example 환경 설정 및 실행 스크립트

echo "========================================"
echo "  MQTT Mosquitto Example Setup"
echo "========================================"

# 1. Conda 환경 생성
echo ""
echo "[1/3] Conda 환경 생성 중..."
if conda env list | grep -q mqtt_mosquitto_example; then
    echo "✓ 환경이 이미 존재합니다."
else
    conda env create -f environment.yml
    echo "✓ 환경 생성 완료"
fi

# 2. Docker Compose로 브로커 시작
echo ""
echo "[2/3] Mosquitto 브로커 시작 중..."
docker-compose up -d
sleep 3

if docker ps | grep -q mqtt-broker; then
    echo "✓ 브로커 시작 완료"
else
    echo "✗ 브로커 시작 실패"
    exit 1
fi

# 3. 사용 안내
echo ""
echo "[3/3] 환경 활성화"
echo ""
echo "========================================"
echo "  ✓ 설정 완료!"
echo "========================================"
echo ""
echo "다음 단계를 따라 테스트하세요:"
echo ""
echo "1. 먼저 conda 환경을 활성화하세요:"
echo "   $ conda activate mqtt_mosquitto_example"
echo ""
echo "2. 새로운 터미널을 열고 Subscriber를 실행하세요:"
echo "   $ conda activate mqtt_mosquitto_example"
echo "   $ python sub_paho_example.py"
echo ""
echo "3. 또 다른 터미널을 열고 Publisher를 실행하세요:"
echo "   $ conda activate mqtt_mosquitto_example"
echo "   $ python pub_paho_example.py"
echo ""
echo "4. Subscriber 터미널에서 메시지를 확인하세요!"
echo ""
echo "브로커를 정지하려면:"
echo "   $ docker-compose down"
echo ""
echo "========================================"
