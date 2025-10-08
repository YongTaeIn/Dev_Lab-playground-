# 🔌 MQTT & AMQP Examples

> English | [한국어](./README.ko.md)

A comprehensive guide comparing MQTT and AMQP protocols with practical examples.

## 📌 What's the Difference?

### MQTT vs AMQP Overview

| Aspect | MQTT | AMQP |
|--------|------|------|
| **Full Name** | Message Queuing Telemetry Transport | Advanced Message Queuing Protocol |
| **Design Goal** | Lightweight IoT messaging | Enterprise message queuing |
| **Protocol Type** | Topic-based Pub/Sub | Queue-based messaging |
| **Overhead** | Very low (~2 bytes header) | Higher (~8 bytes header) |
| **QoS Levels** | 3 levels (0, 1, 2) | Multiple delivery guarantees |
| **Best For** | IoT, Mobile, Sensors | Microservices, Enterprise |
| **Bandwidth** | Low bandwidth optimized | Normal/high bandwidth |
| **Complexity** | Simple | More complex |
| **Routing** | Topic wildcards | Complex exchange routing |

---

## 🔍 Detailed Comparison

### 1️⃣ **Architecture Pattern**

#### MQTT (Topic-based Pub/Sub)
```
Publisher → [Topic: sensor/temperature] → Broker → Subscribers
                                           ↓
                                    All interested clients
```
- Publishers send to **topics**
- Subscribers listen to **topic patterns**
- No direct queue concept
- Many-to-many communication

#### AMQP (Queue-based Messaging)
```
Producer → [Exchange] → [Binding Rules] → [Queue] → Consumer
                ↓
          Routing logic
```
- Producers send to **exchanges**
- Messages routed to **queues** via bindings
- Consumers read from specific queues
- Point-to-point or fan-out patterns

---

### 2️⃣ **Message Delivery Guarantees**

#### MQTT QoS Levels
```
QoS 0: At most once  (Fire and forget)
  → No acknowledgment, fastest, possible loss

QoS 1: At least once (Acknowledged delivery)
  → Guaranteed delivery, possible duplicates

QoS 2: Exactly once  (Four-way handshake)
  → Guaranteed once, slowest, no duplicates
```

#### AMQP Guarantees
```
- Acknowledgments (manual/automatic)
- Transactions support
- Publisher confirms
- Persistent messages (survive broker restart)
- Dead letter queues (failed messages)
```

---

### 3️⃣ **Use Cases**

#### ✅ Use MQTT When:
- Building IoT sensor networks
- Mobile app push notifications
- Real-time location tracking
- Low bandwidth/unstable networks
- Battery-powered devices
- Simple pub/sub needed

**Example:**
```
Smart home: Temperature sensors → MQTT Broker → Mobile app
```

#### ✅ Use AMQP When:
- Microservices communication
- Task queue systems
- Financial transactions
- Order processing pipelines
- Need guaranteed delivery
- Complex routing required

**Example:**
```
E-commerce: Order Service → RabbitMQ → Payment Service → Shipping Service
```

---

### 4️⃣ **Protocol Overhead**

#### MQTT
```python
# Minimal packet structure
Fixed Header: 2 bytes
Variable Header: minimal
Payload: your data

Total overhead: ~2-4 bytes
```

#### AMQP
```python
# More structured packet
Frame Header: 8 bytes
Protocol Header: additional bytes
Content properties: metadata

Total overhead: ~8-12 bytes
```

**Impact:** MQTT is 2-3x lighter for small messages

---

### 5️⃣ **Topic vs Queue Routing**

#### MQTT Topics (Hierarchical)
```
sensor/living-room/temperature
sensor/bedroom/temperature
sensor/+/temperature          # Single-level wildcard
sensor/#                      # Multi-level wildcard
```

#### AMQP Exchanges & Routing
```
Direct Exchange:    Exact routing key match
Fanout Exchange:    Broadcast to all queues
Topic Exchange:     Pattern matching (*, #)
Headers Exchange:   Header-based routing
```

---

## 📚 Examples in This Repository

### 1️⃣ Paho MQTT Example (Mosquitto Broker)

**Protocol:** MQTT  
**Client:** Paho-MQTT  
**Broker:** Mosquitto  

📖 [View Example](./paho_example(mosquitto)/)

---

### 2️⃣ Pika AMQP Example (RabbitMQ Broker)

**Protocol:** AMQP  
**Client:** Pika  
**Broker:** RabbitMQ  

📖 [View Example](./pika_example(rabbitmq)/)

---

## 🎯 Which Should You Choose?

### Choose MQTT if you need:
- ✅ Lightweight protocol
- ✅ Low power consumption
- ✅ Mobile/IoT devices
- ✅ Simple pub/sub
- ✅ Unstable networks
- ✅ Low bandwidth

### Choose AMQP if you need:
- ✅ Guaranteed delivery
- ✅ Complex routing
- ✅ Enterprise features
- ✅ Transaction support
- ✅ Microservices
- ✅ High reliability

---

## 🔧 Performance Comparison

| Metric | MQTT | AMQP |
|--------|------|------|
| **Throughput** | Higher (lighter) | Lower (more overhead) |
| **Latency** | Lower (~1-5ms) | Higher (~5-15ms) |
| **CPU Usage** | Lower | Higher |
| **Memory** | Lower | Higher |
| **Scalability** | Excellent for many clients | Excellent for many queues |

---

## 🌐 Real-World Examples

### MQTT in Action
```
🏠 Smart Home
  - Thermostat publishes: home/temperature
  - App subscribes: home/#
  - Lightbulbs subscribe: home/lights/+

📱 Mobile Chat
  - User sends message to: chat/room123
  - All room members subscribe: chat/room123

🚗 Fleet Tracking
  - Vehicle publishes: fleet/vehicle/{id}/location
  - Control center subscribes: fleet/vehicle/+/location
```

### AMQP in Action
```
🛒 E-commerce Order Processing
  1. Order Service → order.placed queue
  2. Payment Service consumes from order.placed
  3. Payment Service → order.paid queue
  4. Shipping Service consumes from order.paid

📧 Email Service
  - Web app → email.send queue
  - Worker processes consume and send emails
  - Failed emails → dead letter queue

🔄 Microservices
  - API Gateway → multiple service queues
  - Each service has dedicated queue
  - Load balancing across workers
```

---

## 🚀 Quick Start

### Clone Repository
```bash
git clone https://github.com/YongTaeIn/Dev_Lab-playground-.git
cd Dev_Lab-playground-/MQTT_AMQP_example
```

### Try MQTT Example
```bash
cd paho_example(mosquitto)
chmod +x setup.sh
./setup.sh
```

### Try AMQP Example
```bash
cd pika_example(rabbitmq)
chmod +x setup.sh
./setup.sh
```

---

## 📖 Learn More

### MQTT Resources
- [MQTT Official](https://mqtt.org/)
- [Eclipse Paho](https://eclipse.org/paho/)
- [Mosquitto Broker](https://mosquitto.org/)

### AMQP Resources
- [AMQP Specification](https://www.amqp.org/)
- [RabbitMQ Official](https://www.rabbitmq.com/)
- [Pika Documentation](https://pika.readthedocs.io/)

---

## 🤝 Contributing

Contributions welcome! Please submit issues or pull requests.

---

**Happy Messaging! 📨**

_"Different protocols for different needs - choose wisely!"_
