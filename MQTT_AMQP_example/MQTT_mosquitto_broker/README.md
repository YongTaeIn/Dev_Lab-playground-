# MQTT Paho Example

> English | [한국어](./README.ko.md)

A simple Pub/Sub example using Paho-MQTT and Mosquitto broker.

## 🚀 Quick Start

### 1. Environment Setup and Broker Startup
```bash
chmod +x setup.sh
./setup.sh
```

### 2. Terminal 1 - Run Subscriber
```bash
conda activate mqtt_mosquitto_example
python sub_paho_example.py
```

### 3. Terminal 2 - Run Publisher
```bash
conda activate mqtt_mosquitto_example
python pub_paho_example.py
```

### 4. Stop the Broker
```bash
docker-compose down
```

## 📁 File Structure

- `environment.yml`: Conda environment definition
- `docker-compose.yml`: Mosquitto broker configuration
- `setup.sh`: Environment setup and broker startup script
- `pub_paho_example.py`: Publisher code
- `sub_paho_example.py`: Subscriber code
- `mosquitto.conf`: Mosquitto configuration file

## 📡 Port Information

- `1883`: MQTT default port
- `20518`: Test port (used in code)
- `9001`: WebSocket port (optional)

## 🛠️ Troubleshooting

### Check Broker Logs
```bash
docker-compose logs -f
```

### Check Broker Status
```bash
docker ps | grep mqtt-broker
```

### Reset Environment
```bash
conda env remove -n mqtt_mosquitto_example
./setup.sh
```

## 📝 Notes

- Mosquitto 2.0+ requires configuration file for anonymous connections
- The `setup.sh` script handles all the setup automatically
- Make sure Docker is running before executing `setup.sh`
- Use separate terminals for subscriber and publisher for easy testing
