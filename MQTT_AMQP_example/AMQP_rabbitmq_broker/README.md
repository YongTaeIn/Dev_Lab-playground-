# RabbitMQ Pika Example

> English | [한국어](./README.ko.md)

A simple Pub/Sub example using Pika (RabbitMQ Python client) with Docker.

## 🚀 Quick Start

### 1. Environment Setup and Broker Startup
```bash
chmod +x setup.sh
./setup.sh
```

### 2. Terminal 1 - Run Subscriber
```bash
conda activate rabbitmq_pika_example
python sub_using_pika.py
```

### 3. Terminal 2 - Run Publisher
```bash
conda activate rabbitmq_pika_example
python pub_using_pika.py
```

### 4. Stop the Broker
```bash
docker-compose down
```

## 📁 File Structure

- `environment.yml`: Conda environment definition
- `docker-compose.yml`: RabbitMQ broker configuration
- `setup.sh`: Environment setup and broker startup script
- `pub_using_pika.py`: Publisher code
- `sub_using_pika.py`: Subscriber code

## 📡 Port Information

- `5672`: RabbitMQ AMQP port
- `15672`: RabbitMQ Management UI
  - URL: http://localhost:15672
  - Username: `guest`
  - Password: `guest`
- `20518`: Alternative port mapping

## 🔧 Configuration

Update connection parameters in both Python files if needed:
```python
pika.ConnectionParameters(
    'localhost',  # RabbitMQ server address
    5672,         # Port
    '/',          # Virtual host
    pika.PlainCredentials('guest', 'guest')  # Username/Password
)
```

## 🛠️ Troubleshooting

### Check Broker Logs
```bash
docker-compose logs -f rabbitmq
```

### Check Broker Status
```bash
docker ps | grep rabbitmq-broker
```

### Access Management UI
Open browser: http://localhost:15672
- Default credentials: guest/guest
- View queues, exchanges, and messages

### Reset Environment
```bash
conda env remove -n rabbitmq_pika_example
docker-compose down -v  # Remove volumes
./setup.sh
```

## 📝 Notes

- Pika is a pure-Python RabbitMQ client library
- RabbitMQ uses AMQP protocol (Advanced Message Queuing Protocol)
- Queue-based messaging with guaranteed delivery
- Enterprise-grade message broker with clustering support
- The `setup.sh` script handles all setup automatically
- Make sure Docker is running before executing `setup.sh`

## 🆚 AMQP vs MQTT

| Feature | AMQP (RabbitMQ) | MQTT (Mosquitto) |
|---------|-----------------|------------------|
| **Protocol** | AMQP | MQTT |
| **Messaging** | Queue-based | Topic-based |
| **Reliability** | Guaranteed delivery | QoS levels (0,1,2) |
| **Use Case** | Enterprise, Microservices | IoT, Mobile |
| **Overhead** | Higher | Lower |
| **Complexity** | More complex routing | Simple Pub/Sub |
