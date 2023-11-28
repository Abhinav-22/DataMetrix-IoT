import paho.mqtt.client as mqtt
import json
 
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

broker_address = "mqtt5"
port = 1883
topic = "room/sensors"
client_id = "sensor_subscriber"


influx_url = "http://influxdb:8086"
influx_token = "PtyE4Zp1fuRlb9gtfEtGWEoUK0JnHGsVz7y-F8rU02TRyZ7UGCdozrH2flYp1KP14j5Bff4BIjkD1gTAmVPE3A=="
influx_org = "Mosquitto"
influx_bucket = "MQTT"
influx_client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)
 
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))
    client.subscribe(topic)
 
def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    data = json.loads(payload)
 
    temperature = data["properties"]["temperature"]["value"]
    humidity = data["properties"]["humidity"]["value"]
 
    print()
    point1 = Point("Sensor").tag("measure", "humidity").field("value", humidity)
    point2 = Point("Sensor").tag("measure", "temperature").field("value", temperature)


    write_api.write(bucket=influx_bucket, org=influx_org, record=point1)
    write_api.write(bucket=influx_bucket, org=influx_org, record=point2)
    
 
client = mqtt.Client(client_id)
 
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker_address, port)
 
client.loop_forever()
