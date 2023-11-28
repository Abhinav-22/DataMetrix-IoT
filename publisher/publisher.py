import paho.mqtt.client as mqtt
import json
import time
import os



broker_address = os.environ.get("BROKER_ADDRESS", "default_broker")
port = int(os.environ.get("PORT", 1883))
topic = os.environ.get("TOPIC", "default_topic")
client_id = os.environ.get("CLIENT_ID", "default_client_id")

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
