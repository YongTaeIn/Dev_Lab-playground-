# 🎓 Dev Lab Playground

> **Development archive for baseline testing and experiment records**

<div align="right">
  
[🇰🇷 한국어](./README.ko.md) | [🇺🇸 English](./README.md)

</div>

## 📌 Project Purpose

**The goal of this repository is to rapidly acquire core development knowledge for real-world service operations.**

To operate services stably, you need development skills tailored to your service characteristics. Theory alone is insufficient - you must practice hands-on to apply knowledge in real situations.

**This repository provides:**
- ✅ Curated technologies frequently used in production
- ✅ Ready-to-run example code
- ✅ Step-by-step guides for quick learning
- ✅ Real-world use cases for practical understanding

---

## 📚 Project List

### 1️⃣ [Kafka Example](./kafka_example)

**Apache Kafka Fundamentals**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Conda](https://img.shields.io/badge/Conda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://docs.conda.io/)

**🎯 Learning Objectives**  
Understand Kafka Producer/Consumer patterns and build basic message queue systems

**📦 Tech Stack**  
Kafka, Docker, Python, Conda

**💼 Real-World Use Cases**
```
• Asynchronous communication between microservices
  → Order service sends order info to Kafka → Shipping service receives and processes

• Log aggregation system
  → Collect logs from multiple servers via Kafka → Monitor at central log analysis server

• Event-driven architecture
  → Store user behavior events (clicks, purchases) in Kafka → Recommendation & analytics systems consume
```

[📖 View Detailed Guide](./kafka_example/readme.md)

---

### 2️⃣ [Kafka + Flink Example](./kafka_flink_example)

**Real-time Stream Data Processing**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![Flink](https://img.shields.io/badge/Apache%20Flink-E6526F?style=for-the-badge&logo=apache-flink&logoColor=white)](https://flink.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

**🎯 Learning Objectives**  
Build real-time data pipelines combining Kafka and Flink, understand stream processing

**📦 Tech Stack**  
Kafka, Flink, Docker, Python

**💼 Real-World Use Cases**
```
• Real-time anomaly detection system
  → Collect IoT sensor data via Kafka → Flink analyzes in real-time to detect anomalies → Send alerts

• Real-time recommendation system
  → Collect user clickstream via Kafka → Flink analyzes in real-time → Generate personalized recommendations

• Financial transaction monitoring
  → Receive transaction data via Kafka → Flink detects suspicious transaction patterns in real-time → Block risky transactions

• Real-time dashboard
  → Collect service metrics via Kafka → Flink aggregates and calculates → Display on real-time dashboard
```

[📖 View Detailed Guide](./kafka_flink_example/readme.md)

---

### 3️⃣ [Python Asyncio Example](./python_asyncio_example)

**Python Asynchronous Programming**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

**🎯 Learning Objectives**  
Master Python asyncio fundamentals and understand performance optimization

**📦 Tech Stack**  
Python asyncio

**💼 Real-World Use Cases**
```
• API server development
  → Build high-performance async web servers using FastAPI, aiohttp
  → Handle thousands of concurrent requests

• Web crawling/scraping
  → Crawl hundreds of web pages simultaneously
  → 10x+ speed improvement over sequential processing

• Database batch operations
  → Execute multiple DB queries concurrently
  → Minimize I/O wait time

• External API calls
  → Call multiple external service APIs simultaneously to reduce response time
```

[📖 View Detailed Guide](./python_asyncio_example/readme.md)

---

### 4️⃣ [MQTT & AMQP Example](./MQTT_AMQP_example)

**Message Queue Protocols Comparison**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)](https://mqtt.org/)
[![Mosquitto](https://img.shields.io/badge/Mosquitto-3C5280?style=for-the-badge&logo=eclipsemosquitto&logoColor=white)](https://mosquitto.org/)
[![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://www.rabbitmq.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Conda](https://img.shields.io/badge/Conda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://docs.conda.io/)

**🎯 Learning Objectives**  
Understand MQTT and AMQP protocols, compare messaging patterns, and implement IoT and enterprise messaging systems

**📦 Tech Stack**  
MQTT (Paho + Mosquitto), AMQP (Pika + RabbitMQ), Docker, Conda

**💼 Real-World Use Cases**
```
• IoT sensor data collection (MQTT)
  → Temperature sensors publish to MQTT broker → Mobile app subscribes and displays real-time data

• Smart home automation (MQTT)
  → User commands via app → MQTT broker → Smart devices execute commands

• Microservices communication (AMQP)
  → Order service → RabbitMQ queue → Payment service → Shipping service (guaranteed delivery)

• Task queue system (AMQP)
  → Web server publishes background jobs → Worker processes consume from queue and execute
```

[📖 View Detailed Guide](./MQTT_AMQP_example/README.md)

---

## 🚀 Quick Start

### Installation Guide

```bash
# 1. Clone repository
git clone https://github.com/YongTaeIn/Dev_Lab-playground-.git
cd Dev_Lab-playground-

# 2. Select desired project
cd kafka_example  # or kafka_flink_example, python_asyncio_example, MQTT_AMQP_example

# 3. Check README.md and run
cat readme.md
```

---

## 📖 Project Details

### 🔧 Tech Stack Comparison

| Project | Python | Kafka | Flink | MQTT | AMQP | Docker | Conda |
|---------|--------|-------|-------|------|------|--------|-------|
| **Kafka Example** | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Kafka + Flink** | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| **Python Asyncio** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **MQTT & AMQP** | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |

---

## 🤝 Contributing

This project is created for educational purposes, and we welcome improvement suggestions and bug reports!

```bash
# Report Issues
https://github.com/YongTaeIn/Dev_Lab-playground-/issues

# Pull Requests
https://github.com/YongTaeIn/Dev_Lab-playground-/pulls
```

---

## 📞 Contact & Feedback

- **GitHub Issues**: [Create an issue](https://github.com/YongTaeIn/Dev_Lab-playground-/issues)
- **Email**: Please contact us via issues

---

## 📄 License

Example code in this project is freely available for learning and reference purposes.

---

## 🌟 Star History

If this project helped you, please give us a ⭐ Star!

---

<div align="center">

**Happy Learning! 🎓**

*"Learn through practice, grow through experience."*

Made with ❤️ for learners

[⬆ Back to top](#-dev-lab-playground)

</div>
