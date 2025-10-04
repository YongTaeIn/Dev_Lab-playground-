#!/usr/bin/env bash
# SheBang (#!) : 스크립트 파일을 실행할 때 사용하는 인터프리터를 지정


# Kafka(브로커) 시작 스크립트


# 안전 모드: 
#  -e: 명령 실패 시 즉시 종료
#  -u: 정의되지 않은 변수 사용 시 오류
#  -o pipefail: 파이프라인 어느 단계라도 실패하면 전체 실패로 처리


set -euo pipefail

# 스크립트 파일이 있는 디렉터리로 이동(어디서 실행하든 compose 파일을 찾게 함)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "🚀 Starting Kafka Broker..."
docker-compose up -d

echo "⏳ Waiting for Kafka to be ready..."
sleep 10

echo "✅ Kafka is ready!"
echo ""
echo "📝 Next steps:"
echo "  1. Run Producer:  cd Kafka && python producer.py"
echo "  2. Run Flink:     cd Flink && python print_from_kafka.py  (in new terminal)"
echo "  3. Run Consumer:  cd Kafka && python consumer.py          (in new terminal)"
echo ""
echo "🌐 Kafka UI: http://localhost:8080"

