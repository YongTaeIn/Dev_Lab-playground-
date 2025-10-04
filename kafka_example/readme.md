# Kafka Example Project 🚀

<div align="right">

[🇰🇷 한국어](./README.ko.md) | [🇺🇸 English](./README.md)

</div>

A beginner-friendly example project to learn the basics of Apache Kafka.  
Simple hands-on code for sending messages with Producer and receiving them with Consumer.

## 📋 Project Structure

```
Kafka_example/
├── docker_compose.yaml    # Kafka broker + UI configuration
├── producer.py            # Message producer
├── consumer.py            # Message consumer
├── environment.yml        # Conda environment configuration
├── setup.sh               # Automatic setup script
└── readme.md              # This file
```

> ⚠️ **Important**: This project uses **Conda environment**. Conda must be installed.

## 🎯 Learning Objectives

- Easily run Kafka broker with Docker
- Send messages with Producer
- Receive messages with Consumer
- Monitor topics and messages with Kafka UI

## ⚙️ Prerequisites

### Required Installations

1. **Conda (Anaconda or Miniconda)**
   - [Anaconda Download](https://www.anaconda.com/download)
   - [Miniconda Download](https://docs.conda.io/en/latest/miniconda.html) (Lightweight version recommended)

2. **Docker Desktop**
   - [Docker Download](https://www.docker.com/products/docker-desktop/)

---

## ⚙️ Quick Start (Automatic Setup)

**Recommended for beginners!** We provide a script that automatically sets up the environment:

```bash
bash setup.sh
```

This script automatically:
- ✅ Creates Conda virtual environment (`kafka_ver_1`)
- ✅ Installs required Python packages (`kafka-python`)
- ✅ Checks Docker and runs Kafka broker
- ✅ Verifies environment setup completion

After running the script, jump to **Step 3**!

---

## ⚙️ Manual Setup (Step by Step)

If you want to set up manually instead of automatic setup:

### 1. Create Conda Environment

**Method A: Use environment.yml (Recommended)**
```bash
conda env create -f environment.yml
conda activate kafka_ver_1
```

**Method B: Create environment manually**
```bash
conda create -n kafka_ver_1 python=3.9
conda activate kafka_ver_1
pip install kafka-python==2.0.2
```

### 2. Verify Docker is Running
```bash
docker --version
# Check if Docker Desktop is running
```

## 🚀 Execution Steps

> **📌 Note:** If you ran `setup.sh`, skip Steps 1 and 2 and start from **Step 3**!

### Step 1: Run Kafka Broker

Open terminal and navigate to this folder, then run Kafka with Docker Compose:

```bash
cd Kafka_example
docker compose -f docker_compose.yaml up -d
```

**Verify execution:**
```bash
docker ps
```
If `kafka` and `kafka-ui` containers are running, success! ✅

### Step 2: Access Kafka UI (Optional)

Access in browser:
```
http://localhost:8080
```
- View topic list
- Check message contents
- Monitor broker status

### Step 3: Run Producer (Send Messages)

Open a new terminal and run Producer:

```bash
python producer.py
```

**Expected output:**
```
Sent: key=key-0, value=hello 0
Sent: key=key-1, value=hello 1
Sent: key=key-2, value=hello 2
...
Sent: key=key-9, value=hello 9
```

10 messages are sent to `test-topic`! 📤

### Step 4: Run Consumer (Receive Messages)

Open another new terminal and run Consumer:

```bash
python consumer.py
```

**Expected output:**
```
Listening for messages...
test-topic:0:0: key=key-0, value=hello 0
test-topic:0:1: key=key-1, value=hello 1
test-topic:0:2: key=key-2, value=hello 2
...
test-topic:0:9: key=key-9, value=hello 9
```

Receive messages sent by Producer in real-time! 📥

### Step 5: Experiment 🧪

1. **Run Consumer first** (waiting for messages)
2. **Then run Producer**
3. Watch Consumer receive messages in real-time!

Or:
1. Run Producer multiple times to send more messages
2. Run new Consumer to receive all previous messages (`auto_offset_reset='earliest'` setting)

## 🛑 Shutdown and Cleanup

### Terminate Python Programs
Press `Ctrl + C` in each terminal

### Complete System Cleanup
If you want to start fresh:

```bash
# Delete Conda environment
conda deactivate
conda env remove -n kafka_ver_1

# Delete all Docker volumes (including Kafka data)
docker compose -f docker_compose.yaml down -v
```

## 📚 Key Concepts

### Producer
- Sends messages to Kafka topics
- In this example: Sends 10 messages to `test-topic`

### Consumer
- Reads messages from Kafka topics
- Multiple consumers can process messages in parallel through Consumer Group

### Topic
- Logical channel where messages are stored
- In this example: `test-topic`

### Broker
- Kafka server that stores and manages messages
- Runs in Docker container (port: 9092)

## 🔧 Troubleshooting

### 1. `Connection refused` error
→ Check if Kafka broker is running:
```bash
docker ps
```

### 2. `ModuleNotFoundError: No module named 'kafka'`
→ Verify Conda environment is activated:
```bash
conda activate kafka_ver_1
```
→ Or reinstall package:
```bash
pip install kafka-python==2.0.2
```

### 3. Docker container won't start
→ Port may already be in use. Terminate other Kafka instances or change port

### 4. Consumer not receiving messages
→ Verify Producer was executed first
→ Check topic name is identical (`test-topic`)

## 💡 Next Steps

Once you understand this basic example:
1. Run multiple Consumers simultaneously (observe Consumer Group behavior)
2. Try changing topic names
3. Send JSON format messages
4. Add message processing logic (data storage, transformation, etc.)

## 📖 References

- [Apache Kafka Official Documentation](https://kafka.apache.org/documentation/)
- [kafka-python Library](https://kafka-python.readthedocs.io/)

---

**Happy Kafka Learning! 🎓**

