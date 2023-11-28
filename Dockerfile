FROM python:3.11-alpine

WORKDIR /app

COPY sub.py /app/sub.py
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install paho-mqtt influxdb-client



CMD ["python", "sub.py"]