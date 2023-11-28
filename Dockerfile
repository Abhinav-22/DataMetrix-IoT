FROM python:3.11-alpine

WORKDIR /app

COPY sub.py /app/sub.py
COPY requirements.txt /app/requirements.txt

ENV BROKER_ADDRESS="mqtt5"
ENV PORT=1883
ENV TOPIC="room/sensors"
ENV CLIENT_ID="sensor_subscriber"

ENV INFLUX_URL="http://influxdb:8086"
ENV INFLUX_TOKEN="PtyE4Zp1fuRlb9gtfEtGWEoUK0JnHGsVz7y-F8rU02TRyZ7UGCdozrH2flYp1KP14j5Bff4BIjkD1gTAmVPE3A=="
ENV INFLUX_ORG="Mosquitto"
ENV INFLUX_BUCKET="MQTT"

RUN pip install --upgrade pip
RUN pip install paho-mqtt influxdb-client



CMD ["python", "sub.py"]