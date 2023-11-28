FROM python:3.11-alpine

WORKDIR /app

COPY publisher.py /app/publisher.py


ENV BROKER_ADDRESS="mqtt5"
ENV PORT=1883
ENV TOPIC="room/sensors"
ENV CLIENT_ID="sensor_subscriber"

RUN pip install --upgrade pip
RUN pip install paho-mqtt 



CMD ["python", "publisher.py"]