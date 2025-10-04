#!/bin/bash

# Kafka Example 환경 설정 스크립트
# 사용법: bash setup.sh

echo "=================================="
echo "Kafka Example 환경 설정 시작 🚀"
echo "=================================="
echo ""

# 1. Conda 환경 생성
echo "📦 Step 1: Conda 가상환경 생성 중..."
conda env list | grep kafka_ver_1 > /dev/null
if [ $? -eq 0 ]; then
    echo "   ⚠️  kafka_ver_1 환경이 이미 존재합니다."
    read -p "   삭제하고 다시 만드시겠습니까? (y/n): " answer
    if [ "$answer" = "y" ]; then
        conda env remove -n kafka_ver_1 -y
        conda env create -f environment.yml
        echo "   ✅ 환경을 다시 만들었습니다."
    else
        echo "   ⏭️  기존 환경을 사용합니다."
    fi
else
    conda env create -f environment.yml
    echo "   ✅ kafka_ver_1 환경 생성 완료!"
fi
echo ""

# 2. Docker 확인
echo "🐳 Step 2: Docker 실행 확인 중..."
if ! docker info > /dev/null 2>&1; then
    echo "   ❌ Docker가 실행되지 않았습니다."
    echo "   Docker Desktop을 실행한 후 다시 시도해주세요."
    exit 1
else
    echo "   ✅ Docker가 실행 중입니다!"
fi
echo ""

# 3. Kafka 컨테이너 실행
echo "☕ Step 3: Kafka 브로커 실행 중..."
docker compose -f docker_compose.yaml up -d
if [ $? -eq 0 ]; then
    echo "   ✅ Kafka 브로커 실행 완료!"
else
    echo "   ❌ Kafka 브로커 실행 실패"
    exit 1
fi
echo ""

# 4. 컨테이너 상태 확인
echo "🔍 Step 4: 컨테이너 상태 확인..."
sleep 3
docker ps --filter "name=kafka" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""

# 완료 메시지
echo "=================================="
echo "✅ 환경 설정 완료!"
echo "=================================="
echo ""
echo "📌 다음 단계:"
echo "1. 가상환경 활성화:"
echo "   conda activate kafka_ver_1"
echo ""
echo "2. Producer 실행 (메시지 전송):"
echo "   python producer.py"
echo ""
echo "3. Consumer 실행 (메시지 수신):"
echo "   python consumer.py"
echo ""
echo "4. Kafka UI 접속 (브라우저):"
echo "   http://localhost:8080"
echo ""
echo "Happy Kafka Learning! 🎓"

