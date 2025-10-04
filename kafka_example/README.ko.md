# Kafka 예제 프로젝트 🚀

<div align="right">

[🇰🇷 한국어](./README.ko.md) | [🇺🇸 English](./README.md)

</div>

Apache Kafka의 기본 개념을 배우기 위한 초보자용 예제입니다.  
Producer가 메시지를 전송하고, Consumer가 메시지를 받아오는 간단한 실습 코드입니다.

## 📋 프로젝트 구성

```
Kafka_example/
├── docker_compose.yaml    # Kafka 브로커 + UI 실행 설정
├── producer.py            # 메시지를 보내는 생산자
├── consumer.py            # 메시지를 받는 소비자
├── environment.yml        # Conda 환경 설정 파일
├── setup.sh               # 자동 환경 설정 스크립트
└── readme.md              # 이 파일
```

> ⚠️ **중요**: 이 프로젝트는 **Conda 환경**을 사용합니다. Conda가 설치되어 있어야 합니다.

## 🎯 학습 목표

- Kafka 브로커를 Docker로 쉽게 실행하기
- Producer로 메시지 전송하기
- Consumer로 메시지 수신하기
- Kafka UI로 토픽과 메시지 모니터링하기

## ⚙️ 사전 요구사항

### 필수 설치 항목

1. **Conda (Anaconda 또는 Miniconda)**
   - [Anaconda 다운로드](https://www.anaconda.com/download)
   - [Miniconda 다운로드](https://docs.conda.io/en/latest/miniconda.html) (가벼운 버전 추천)

2. **Docker Desktop**
   - [Docker 다운로드](https://www.docker.com/products/docker-desktop/)

---

## ⚙️ 빠른 시작 (자동 설정)

**초보자 추천!** 모든 환경을 자동으로 설정하는 스크립트를 제공합니다:

```bash
bash setup.sh
```

이 스크립트가 자동으로:
- ✅ Conda 가상환경 생성 (`kafka_ver_1`)
- ✅ 필요한 Python 패키지 설치 (`kafka-python`)
- ✅ Docker 확인 및 Kafka 브로커 실행
- ✅ 환경 설정 완료 확인

스크립트 실행 후 바로 **Step 3**으로 이동하세요!

---

## ⚙️ 수동 설정 (단계별)

자동 설정 대신 직접 설정하고 싶다면:

### 1. Conda 환경 생성

**방법 A: environment.yml 사용 (추천)**
```bash
conda env create -f environment.yml
conda activate kafka_ver_1
```

**방법 B: 수동으로 환경 생성**
```bash
conda create -n kafka_ver_1 python=3.9
conda activate kafka_ver_1
pip install kafka-python==2.0.2
```

### 2. Docker 실행 확인
```bash
docker --version
# Docker Desktop이 실행 중인지 확인
```

## 🚀 실행 방법 (단계별)

> **📌 Note:** `setup.sh`를 실행했다면 Step 1, 2는 건너뛰고 **Step 3**부터 시작하세요!

### Step 1: Kafka 브로커 실행

터미널을 열고 이 폴더로 이동한 후, Docker Compose로 Kafka를 실행합니다:

```bash
cd Kafka_example
docker compose -f docker_compose.yaml up -d
```

**실행 확인:**
```bash
docker ps
```
`kafka`와 `kafka-ui` 컨테이너가 실행 중이면 성공! ✅

### Step 2: Kafka UI 접속 (선택사항)

브라우저에서 아래 주소로 접속하면 Kafka 상태를 시각적으로 확인할 수 있습니다:
```
http://localhost:8080
```
- 토픽 목록 확인
- 메시지 내용 확인
- 브로커 상태 모니터링

### Step 3: Producer 실행 (메시지 전송)

새로운 터미널을 열고 Producer를 실행합니다:

```bash
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

`test-topic`이라는 토픽으로 10개의 메시지가 전송됩니다! 📤

### Step 4: Consumer 실행 (메시지 수신)

또 다른 터미널을 열고 Consumer를 실행합니다:

```bash
python consumer.py
```

**예상 출력:**
```
Listening for messages...
test-topic:0:0: key=key-0, value=hello 0
test-topic:0:1: key=key-1, value=hello 1
test-topic:0:2: key=key-2, value=hello 2
...
test-topic:0:9: key=key-9, value=hello 9
```

Producer가 보낸 메시지를 실시간으로 받아옵니다! 📥

### Step 5: 실험해보기 🧪

1. **Consumer를 먼저 실행**한 후 (메시지 대기 중)
2. **Producer를 실행**하면
3. Consumer가 실시간으로 메시지를 받는 것을 확인할 수 있습니다!

또는:
1. Producer를 여러 번 실행해서 메시지를 더 보내고
2. 새로운 Consumer를 실행하면 이전 메시지도 모두 받아옵니다 (`auto_offset_reset='earliest'` 설정 덕분)

## 🛑 종료 방법

### Consumer 종료
터미널에서 `Ctrl + C` 입력

### Kafka 브로커 종료
```bash
docker compose -f docker_compose.yaml down
```

### 환경 완전 삭제 (선택사항)
모든 것을 처음부터 다시 시작하고 싶다면:

```bash
# Conda 환경 삭제
conda deactivate
conda env remove -n kafka_ver_1

# Docker 볼륨까지 모두 삭제 (Kafka 데이터 포함)
docker compose -f docker_compose.yaml down -v
```

## 📚 주요 개념 설명

### Producer (생산자)
- 메시지를 Kafka 토픽에 전송하는 역할
- 이 예제: `test-topic`에 10개의 메시지 전송

### Consumer (소비자)
- Kafka 토픽에서 메시지를 읽어오는 역할
- Consumer Group을 통해 여러 Consumer가 메시지를 나눠서 처리 가능

### Topic (토픽)
- 메시지가 저장되는 논리적인 채널
- 이 예제: `test-topic`

### Broker (브로커)
- Kafka 서버, 메시지를 저장하고 관리
- Docker 컨테이너로 실행 (port: 9092)

## 🔧 문제 해결

### 1. `Connection refused` 에러
→ Kafka 브로커가 실행 중인지 확인:
```bash
docker ps
```

### 2. `ModuleNotFoundError: No module named 'kafka'`
→ Conda 환경이 활성화되었는지 확인:
```bash
conda activate kafka_ver_1
```
→ 또는 패키지 재설치:
```bash
pip install kafka-python==2.0.2
```

### 3. Docker 컨테이너가 시작되지 않음
→ 포트가 이미 사용 중일 수 있습니다. 다른 Kafka 인스턴스를 종료하거나 포트 변경

### 4. Consumer가 메시지를 받지 못함
→ Producer를 먼저 실행했는지 확인
→ 토픽 이름이 동일한지 확인 (`test-topic`)

## 💡 다음 단계

이 기본 예제를 이해했다면:
1. 여러 Consumer를 동시에 실행해보기 (Consumer Group 동작 확인)
2. 토픽명을 변경해보기
3. 메시지 내용을 JSON 형태로 전송해보기
4. 메시지 처리 로직 추가하기 (데이터 저장, 변환 등)

## 📖 참고 자료

- [Apache Kafka 공식 문서](https://kafka.apache.org/documentation/)
- [kafka-python 라이브러리](https://kafka-python.readthedocs.io/)

---

**Happy Kafka Learning! 🎓**