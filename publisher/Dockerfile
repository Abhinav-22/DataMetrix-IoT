FROM python:3.11-alpine

WORKDIR /app

COPY publisher.py /app/publisher.py

RUN pip install --upgrade pip
RUN pip install paho-mqtt 



CMD ["python", "publisher.py"]