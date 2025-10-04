# Kafka + Flink 실시간 스트림 처리 예제 🚀

Apache Kafka와 Apache Flink를 결합하여 **실시간 데이터 스트림을 처리**하는 방법을 배우는 초보자용 예제입니다.

## 🎯 학습 목표

- Kafka와 Flink를 함께 사용하는 방법 이해하기
- 실시간 데이터 파이프라인 구축하기
- 스트림 데이터 변환 및 처리 실습하기
- Producer → Kafka Broker → Flink → Kafka Broker → Consumer 데이터 흐름 체험하기

## 📋 프로젝트 구조

```
Kafka_Flink_example/
├── Kafka/
│   ├── docker-compose.yml    # Kafka 브로커 + UI 실행 설정
│   ├── producer.py            # 데이터 생성기 (raw-topic에 전송)
│   └── consumer.py            # 데이터 수신기 (processed-topic에서 읽기)
├── Flink/
│   ├── flink_kafka_pipeline.py                  # Flink 스트림 처리 파이프라인
│   └── flink-sql-connector-kafka-*.jar          # Kafka 커넥터 (필수)
└── readme.md
```

## 🔄 데이터 흐름 (전체 파이프라인)

```
┌─────────────┐     ┌──────────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌─────────────┐
│  Producer   │ ──> │  Kafka Broker    │ ──> │    Flink     │ ──> │  Kafka Broker    │ ──> │  Consumer   │
│ producer.py │     │   raw-topic      │     │  Pipeline    │     │ processed-topic  │     │consumer.py  │
└─────────────┘     └──────────────────┘     └──────────────┘     └──────────────────┘     └─────────────┘
  데이터 생성           메시지 저장              실시간 변환             처리 결과 저장            결과 수신
  "hello 0"          "hello 0"           "Processed:          "Processed:            "Processed:
  "hello 1"          "hello 1"            hello 0"             hello 0"               hello 0"
  "hello 2"          "hello 2"            hello 1"             hello 1"               hello 1"
    ...                ...                  ...                  ...                    ...
```

**Kafka Broker (중심 역할):**
- 모든 메시지를 토픽에 저장하고 관리
- Producer와 Consumer 사이의 안정적인 중개자
- 데이터 영속성과 확장성 제공

### 📊 각 단계 설명

| 단계 | 구성 요소 | 역할 | 토픽/포트 |
|------|----------|------|----------|
| 1️⃣ **데이터 생성** | `producer.py` | 원본 데이터를 Kafka에 전송 | → `raw-topic` |
| 2️⃣ **데이터 저장** | **Kafka Broker** | 원본 데이터 저장 및 관리 | `raw-topic` (port 19092) |
| 3️⃣ **데이터 읽기** | `flink_kafka_pipeline.py` | Broker에서 데이터 읽기 | `raw-topic` → |
| 4️⃣ **데이터 처리** | `flink_kafka_pipeline.py` | 실시간 변환 및 가공 | 변환 로직 실행 |
| 5️⃣ **결과 저장** | **Kafka Broker** | 처리된 데이터 저장 | `processed-topic` (port 19092) |
| 6️⃣ **데이터 소비** | `consumer.py` | 처리된 결과 수신 및 출력 | `processed-topic` → |

## 🚀 실행 방법 (단계별)

### Step 1: Kafka 브로커 실행

터미널을 열고 Kafka 폴더로 이동:

```bash
cd Kafka_Flink_example/Kafka
docker compose up -d
```

**실행 확인:**
```bash
docker ps
```
`kafka_broker`와 `kafka-ui` 컨테이너가 실행 중이면 성공! ✅

### Step 2: Kafka UI 접속 (선택사항)

브라우저에서 아래 주소로 접속:
```
http://localhost:8080
```
- **raw-topic**: Producer가 보낸 원본 데이터 확인
- **processed-topic**: Flink가 처리한 결과 데이터 확인

### Step 3: Flink 파이프라인 실행 (데이터 처리기)

**새 터미널**을 열고 Flink 파이프라인을 실행:

```bash
cd Kafka_Flink_example/Flink
python flink_kafka_pipeline.py
```

**예상 출력:**
```
실행 중... (Flink가 Kafka의 데이터를 기다리는 중)
```

Flink가 실행되면 `raw-topic`의 데이터를 읽어서 변환한 후 `processed-topic`에 저장합니다.

### Step 4: Producer 실행 (데이터 생성)

**새 터미널**을 열고 Producer를 실행:

```bash
cd Kafka_Flink_example/Kafka
python producer.py
```

**예상 출력:**
```
Sent: key=key-0, value=hello 0
Sent: key=key-1, value=hello 1
Sent: key=key-2, value=hello 2
...
Sent: key=key-9, value=hello 9
```

10개의 메시지가 `raw-topic`으로 전송됩니다! 📤

이때 **Flink 터미널**에서 실시간 처리 결과가 출력됩니다:
```
Processed: hello 0
Processed: hello 1
Processed: hello 2
...
```

### Step 5: Consumer 실행 (처리된 데이터 수신)

**새 터미널**을 열고 Consumer를 실행:

```bash
cd Kafka_Flink_example/Kafka
python consumer.py
```

**예상 출력:**
```
Listening for messages...
processed-topic:0:0: key=None, value=Processed: hello 0
processed-topic:0:1: key=None, value=Processed: hello 1
processed-topic:0:2: key=None, value=Processed: hello 2
...
```

Flink가 처리한 데이터를 실시간으로 받아옵니다! 📥

## 🎓 핵심 개념 이해하기

### 🔹 Kafka Broker의 역할 (핵심!)
- **메시지 저장소**: 데이터를 토픽에 영구 저장
- **중개자**: Producer와 Consumer를 분리 (독립적으로 동작)
- **버퍼**: 데이터 생산 속도와 소비 속도 차이 해소
- **확장성**: 대용량 데이터를 안정적으로 처리
- **다중 소비**: 하나의 메시지를 여러 Consumer가 읽을 수 있음

### 🔹 Flink의 역할
- **스트림 프로세서**: 실시간 데이터 변환 및 처리
- **ETL**: 데이터 추출(Extract) → 변환(Transform) → 적재(Load)
- **분석 엔진**: 복잡한 데이터 집계 및 계산

### 🔹 왜 Kafka + Flink를 함께 사용하나?

| 시스템 | 강점 | 약점 |
|--------|------|------|
| **Kafka 단독** | ✅ 데이터 저장/전달 | ❌ 복잡한 변환/분석 불가 |
| **Flink 단독** | ✅ 강력한 데이터 처리 | ❌ 영속성/버퍼 없음 |
| **Kafka + Flink** | ✅✅ 저장 + 처리 모두 가능 | 🎯 완벽한 조합! |

### 🔹 실제 사용 사례

```python
# 예제에서는 간단한 변환만 하지만...
transformed = ds.map(lambda x: f"Processed: {x}")

# 실무에서는 이런 작업을 합니다:
# 1. 이상 탐지: 센서 데이터에서 비정상 값 찾기
# 2. 집계: 최근 1분간 평균 온도 계산
# 3. 필터링: 특정 조건의 데이터만 선택
# 4. 조인: 여러 스트림 데이터 결합
# 5. 윈도우 분석: 시간 기반 데이터 그룹화
```

## 📚 각 파일 상세 설명

### 1️⃣ `Kafka/producer.py`

**역할**: 원본 데이터를 생성하여 Kafka의 `raw-topic`에 전송

**주요 코드:**
```python
producer = KafkaProducer(bootstrap_servers=['localhost:19092'])
producer.send('raw-topic', key=f'key-{i}', value=f'hello {i}')
```

**포인트:**
- 포트 `19092` 사용 (Docker 컨테이너와 통신)
- 10개의 메시지를 순차적으로 전송
- 각 메시지는 key-value 쌍으로 구성

### 2️⃣ `Kafka/consumer.py`

**역할**: Flink가 처리한 데이터를 `processed-topic`에서 읽어 출력

**주요 코드:**
```python
consumer = KafkaConsumer(
    'processed-topic',
    bootstrap_servers=['127.0.0.1:19092'],
    auto_offset_reset='latest'  # 최신 메시지부터 읽기
)
```

**포인트:**
- `processed-topic` 구독 (Flink의 출력 토픽)
- `latest` 옵션: Consumer 실행 이후의 메시지만 읽음
- 실시간으로 계속 대기하며 새 메시지 수신

### 3️⃣ `Flink/flink_kafka_pipeline.py`

**역할**: Kafka의 데이터를 읽어 변환한 후 다시 Kafka에 저장

**데이터 흐름:**
```python
# 1. Kafka에서 읽기
source = KafkaSource.builder()
    .set_topics("raw-topic")
    .build()

# 2. 데이터 변환
transformed = ds.map(lambda x: f"Processed: {x}")

# 3. 콘솔 출력 (모니터링)
transformed.print()

# 4. Kafka에 쓰기
sink = KafkaSink.builder()
    .set_topic("processed-topic")
    .build()
transformed.sink_to(sink)
```

**포인트:**
- **Source**: `raw-topic`에서 데이터 읽기
- **Transformation**: 메시지 앞에 "Processed: " 추가
- **Sink**: 변환된 데이터를 `processed-topic`에 저장
- **JAR 파일**: Kafka 커넥터가 필수 (Flink와 Kafka 연결)

### 4️⃣ `Kafka/docker-compose.yml`

**역할**: Kafka 브로커와 UI를 Docker 컨테이너로 실행

**제공하는 서비스:**
```yaml
kafka:          # Kafka 브로커 (port 19092)
kafka-ui:       # 웹 UI (port 8080)
```

**포인트:**
- KRaft 모드 (Zookeeper 불필요)
- 포트 19092로 외부 접속 가능
- Kafka UI로 토픽/메시지 시각화

## 🔧 문제 해결

### 1. `Connection refused` 에러
→ Kafka 브로커가 실행 중인지 확인:
```bash
docker ps
# kafka_broker 컨테이너 확인
```

### 2. Flink에서 `No module named 'pyflink'` 에러
→ Apache Flink 설치:
```bash
pip install apache-flink
```

### 3. Consumer가 메시지를 못 받음
→ 실행 순서 확인:
1. Kafka 브로커 실행
2. Flink 파이프라인 실행
3. Producer 실행 (데이터 생성)
4. Consumer 실행 (결과 수신)

### 4. JAR 파일 경로 오류
→ `flink-sql-connector-kafka-3.1.0-1.18.jar` 파일이 `Flink/` 폴더에 있는지 확인

## 🛑 종료 방법

### 1. Python 프로그램 종료
각 터미널에서 `Ctrl + C` 입력

### 2. Kafka 브로커 종료
```bash
cd Kafka
docker compose down
```

## 💡 실험 아이디어

기본 예제를 이해했다면 다음을 시도해보세요:

### 1. 데이터 변환 로직 수정
```python
# flink_kafka_pipeline.py 수정
# 현재: lambda x: f"Processed: {x}"
# 변경: lambda x: x.upper()  # 대문자로 변환
# 변경: lambda x: f"[{datetime.now()}] {x}"  # 타임스탬프 추가
```

### 2. 필터링 추가
```python
# 짝수 인덱스만 처리
filtered = ds.filter(lambda x: int(x.split()[-1]) % 2 == 0)
```

### 3. 더 많은 데이터 생성
```python
# producer.py 수정
for i in range(100):  # 10 → 100으로 변경
```

### 4. 실시간 통계
```python
# Flink에서 데이터 개수 세기, 평균 계산 등
```

## 📖 참고 자료

- [Apache Kafka 공식 문서](https://kafka.apache.org/documentation/)
- [Apache Flink 공식 문서](https://flink.apache.org/)
- [PyFlink 가이드](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/python/overview/)


---

**Happy Streaming! 🎓**

Kafka로 데이터를 전달하고, Flink로 실시간 처리하는 강력한 파이프라인을 경험하세요!

