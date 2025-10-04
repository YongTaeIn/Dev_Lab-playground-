# Kafka + Flink Real-time Stream Processing Example 🚀

<div align="right">

[🇰🇷 한국어](./README.ko.md) | [🇺🇸 English](./README.md)

</div>

A beginner-friendly example to learn **real-time data stream processing** by combining Apache Kafka and Apache Flink.

## 🎯 Learning Objectives

- Understand how to use Kafka and Flink together
- Build real-time data pipelines
- Practice stream data transformation and processing
- Experience data flow: Producer → Kafka Broker → Flink → Kafka Broker → Consumer

## 📋 Project Structure

```
Kafka_Flink_example/
├── Kafka/
│   ├── docker-compose.yml    # Kafka broker + UI configuration
│   ├── producer.py            # Data generator (sends to raw-topic)
│   └── consumer.py            # Data receiver (reads from processed-topic)
├── Flink/
│   ├── flink_kafka_pipeline.py                  # Flink stream processing pipeline
│   └── flink-sql-connector-kafka-*.jar          # Kafka connector (required)
└── readme.md                  # Practice guide
```

## 🔄 Data Flow (Complete Pipeline)

```
┌─────────────┐     ┌──────────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌─────────────┐
│  Producer   │ ──> │  Kafka Broker    │ ──> │    Flink     │ ──> │  Kafka Broker    │ ──> │  Consumer   │
│ producer.py │     │   raw-topic      │     │  Pipeline    │     │ processed-topic  │     │consumer.py  │
└─────────────┘     └──────────────────┘     └──────────────┘     └──────────────────┘     └─────────────┘
  Data Creation      Message Storage        Real-time Transform    Result Storage          Result Reception
  "hello 0"          "hello 0"              "Processed:            "Processed:             "Processed:
  "hello 1"          "hello 1"               hello 0"               hello 0"                hello 0"
  "hello 2"          "hello 2"               hello 1"               hello 1"                hello 1"
    ...                ...                     ...                    ...                     ...
```

**Kafka Broker (Central Role):**
- Stores and manages all messages in topics
- Reliable intermediary between Producer and Consumer
- Provides data persistence and scalability

### 📊 Step-by-Step Breakdown

| Step | Component | Role | Topic/Port |
|------|----------|------|-----------|
| 1️⃣ **Data Creation** | `producer.py` | Send raw data to Kafka | → `raw-topic` |
| 2️⃣ **Data Storage** | **Kafka Broker** | Store and manage raw data | `raw-topic` (port 19092) |
| 3️⃣ **Data Reading** | `flink_kafka_pipeline.py` | Read data from Broker | `raw-topic` → |
| 4️⃣ **Data Processing** | `flink_kafka_pipeline.py` | Real-time transformation | Execute transform logic |
| 5️⃣ **Result Storage** | **Kafka Broker** | Store processed data | `processed-topic` (port 19092) |
| 6️⃣ **Data Consumption** | `consumer.py` | Receive and output results | `processed-topic` → |

## 🚀 Execution Steps

### Step 1: Run Kafka Broker

Open terminal and navigate to Kafka folder:

```bash
cd Kafka_Flink_example/Kafka
docker compose up -d
```

**Verify execution:**
```bash
docker ps
```
If `kafka_broker` and `kafka-ui` containers are running, success! ✅

### Step 2: Access Kafka UI (Optional)

Access in browser:
```
http://localhost:8080
```
- **raw-topic**: Check raw data sent by Producer
- **processed-topic**: Check result data processed by Flink

### Step 3: Run Flink Pipeline (Data Processor)

Open a **new terminal** and run Flink pipeline:

```bash
cd Kafka_Flink_example/Flink
python flink_kafka_pipeline.py
```

**Expected output:**
```
Running... (Flink is waiting for Kafka data)
```

When Flink runs, it reads data from `raw-topic`, transforms it, and stores it in `processed-topic`.

### Step 4: Run Producer (Generate Data)

Open a **new terminal** and run Producer:

```bash
cd Kafka_Flink_example/Kafka
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

10 messages are sent to `raw-topic`! 📤

At this time, real-time processing results are displayed in **Flink terminal**:
```
Processed: hello 0
Processed: hello 1
Processed: hello 2
...
```

### Step 5: Run Consumer (Receive Processed Data)

Open a **new terminal** and run Consumer:

```bash
cd Kafka_Flink_example/Kafka
python consumer.py
```

**Expected output:**
```
Listening for messages...
processed-topic:0:0: key=None, value=Processed: hello 0
processed-topic:0:1: key=None, value=Processed: hello 1
processed-topic:0:2: key=None, value=Processed: hello 2
...
```

Receive data processed by Flink in real-time! 📥

### Step 6: Shutdown Complete System

When you finish the practice, clean up all containers and data:

```bash
cd Kafka_Flink_example/Kafka
docker compose down -v
```

**Meaning of `-v` option:**
- Stop and remove containers
- Remove networks
- **Delete volumes** (Delete all message data stored in Kafka)

**Warning:** Using `-v` option completely deletes all topics and messages stored in Kafka. You can start fresh for next practice.

> 💡 **Tip**: If you want to keep data, use only `docker compose down` without `-v`.

## 🎓 Understanding Key Concepts

### 🔹 Kafka Broker's Role (Core!)
- **Message Store**: Permanently stores data in topics
- **Intermediary**: Separates Producer and Consumer (operate independently)
- **Buffer**: Resolves differences between data production and consumption speeds
- **Scalability**: Handles large volumes of data reliably
- **Multiple Consumers**: One message can be read by multiple Consumers

### 🔹 Flink's Role
- **Stream Processor**: Real-time data transformation and processing
- **ETL**: Extract → Transform → Load data
- **Analytics Engine**: Complex data aggregation and calculation

### 🔹 Why Use Kafka + Flink Together?

| System | Strengths | Weaknesses |
|--------|-----------|------------|
| **Kafka Alone** | ✅ Data storage/delivery | ❌ Cannot handle complex transformation/analysis |
| **Flink Alone** | ✅ Powerful data processing | ❌ No persistence/buffer |
| **Kafka + Flink** | ✅✅ Both storage + processing | 🎯 Perfect combination! |

### 🔹 Real-World Use Cases

```python
# In this example, we only do simple transformation...
transformed = ds.map(lambda x: f"Processed: {x}")

# But in production, you do things like:
# 1. Anomaly Detection: Find abnormal values in sensor data
# 2. Aggregation: Calculate average temperature over last 1 minute
# 3. Filtering: Select only data meeting specific conditions
# 4. Join: Combine multiple stream data
# 5. Window Analysis: Group data based on time
```

## 📚 Detailed File Descriptions

### 1️⃣ `Kafka/producer.py`

**Role**: Generate raw data and send to Kafka's `raw-topic`

**Key Code:**
```python
producer = KafkaProducer(bootstrap_servers=['localhost:19092'])
producer.send('raw-topic', key=f'key-{i}', value=f'hello {i}')
```

**Key Points:**
- Uses port `19092` (communicates with Docker container)
- Sends 10 messages sequentially
- Each message consists of key-value pair

### 2️⃣ `Kafka/consumer.py`

**Role**: Read data processed by Flink from `processed-topic` and output

**Key Code:**
```python
consumer = KafkaConsumer(
    'processed-topic',
    bootstrap_servers=['127.0.0.1:19092'],
    auto_offset_reset='latest'  # Read from latest messages
)
```

**Key Points:**
- Subscribes to `processed-topic` (Flink's output topic)
- `latest` option: Reads only messages after Consumer starts
- Continuously waits and receives new messages in real-time

### 3️⃣ `Flink/flink_kafka_pipeline.py`

**Role**: Read data from Kafka, transform it, and save back to Kafka

**Data Flow:**
```python
# 1. Read from Kafka
source = KafkaSource.builder()
    .set_topics("raw-topic")
    .build()

# 2. Transform data
transformed = ds.map(lambda x: f"Processed: {x}")

# 3. Print to console (monitoring)
transformed.print()

# 4. Write to Kafka
sink = KafkaSink.builder()
    .set_topic("processed-topic")
    .build()
transformed.sink_to(sink)
```

**Key Points:**
- **Source**: Read data from `raw-topic`
- **Transformation**: Add "Processed: " prefix to messages
- **Sink**: Save transformed data to `processed-topic`
- **JAR File**: Kafka connector is required (connects Flink and Kafka)

### 4️⃣ `Kafka/docker-compose.yml`

**Role**: Run Kafka broker and UI as Docker containers

**Provided Services:**
```yaml
kafka:          # Kafka broker (port 19092)
kafka-ui:       # Web UI (port 8080)
```

**Key Points:**
- KRaft mode (Zookeeper not required)
- External access via port 19092
- Visualize topics/messages with Kafka UI

## 🔧 Troubleshooting

### 1. `Connection refused` error
→ Check if Kafka broker is running:
```bash
docker ps
# Check kafka_broker container
```

### 2. `No module named 'pyflink'` error in Flink
→ Install Apache Flink:
```bash
pip install apache-flink
```

### 3. Consumer not receiving messages
→ Verify execution order:
1. Run Kafka broker
2. Run Flink pipeline
3. Run Producer (generate data)
4. Run Consumer (receive results)

### 4. JAR file path error
→ Verify `flink-sql-connector-kafka-3.1.0-1.18.jar` file exists in `Flink/` folder

## 🛑 Shutdown and Cleanup

### Terminate Python Programs
Press `Ctrl + C` in each terminal to stop running programs.

### Complete System Cleanup
Refer to **Step 6** above to clean up Docker containers and data.

## 💡 Experiment Ideas

Once you understand the basic example, try these:

### 1. Modify Data Transformation Logic
```python
# Modify flink_kafka_pipeline.py
# Current: lambda x: f"Processed: {x}"
# Change to: lambda x: x.upper()  # Convert to uppercase
# Change to: lambda x: f"[{datetime.now()}] {x}"  # Add timestamp
```

### 2. Add Filtering
```python
# Process only even indices
filtered = ds.filter(lambda x: int(x.split()[-1]) % 2 == 0)
```

### 3. Generate More Data
```python
# Modify producer.py
for i in range(100):  # Change 10 → 100
```

### 4. Real-time Statistics
```python
# Count data, calculate averages, etc. in Flink
```

## 📖 References

- [Apache Kafka Official Documentation](https://kafka.apache.org/documentation/)
- [Apache Flink Official Documentation](https://flink.apache.org/)
- [PyFlink Guide](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/python/overview/)

---

**Happy Streaming! 🎓**

Experience the powerful pipeline of delivering data with Kafka and processing in real-time with Flink!

