# DataMetrix-IoT

### DataMetrix-IoT is a comprehensive Internet of Things (IoT) solution for collecting, processing, and visualizing sensor data. The project focuses on monitoring temperature and humidity, employing a robust architecture where sensor data is published, brokered, and stored before being visualized in real-time using Grafana.

---

# Components

- Publisher : Publishes sensor data for temperature and humidity.
- Subscriber : Transfers sensor data to InfluxDB for efficient storage.
- MQTT Broker : Facilitates communication between the publisher and subscriber components.
- InfluxDB : Stores time-series data in a scalable and organized manner.
- Grafana : Provides a user-friendly interface for real-time data visualization.

---

# Getting Started

1. Clone the repository.
2. Set up your MQTT broker and configure environment variables.
3. Build and launch Docker containers for the publisher, subscriber, Grafana, InfluxDB, and MQTT broker.
4. Access Grafana to explore and visualize temperature and humidity data.

