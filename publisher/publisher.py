import paho.mqtt.client as mqtt
import json
import time

broker_address = "mqtt5"
port = 1883
topic = "room/sensors"
client_id = "sensor_publisher_simulator"

data = {
    
    "title": "Sensors",
    "description": "Temperature Humidity Sensor",
    "properties": {
        "temperature": {
            
            "title": "Temperature",
            "type": "number",
            "unit": "Celsius",
            "value": 32
        },
        "humidity": {
            "title": "Humidity",
            "type": "number",
            "unit": "HA",
            "value": 33
        },
      
    }
}

message = json.dumps(data)

client = mqtt.Client(client_id)

client.connect(broker_address, port)

try:
    while True:
        client.publish(topic, message)

        print(f"Published data: {message}")
        time.sleep(3)  
except KeyboardInterrupt:
    client.disconnect()
    print("Disconnected from the MQTT broker")
