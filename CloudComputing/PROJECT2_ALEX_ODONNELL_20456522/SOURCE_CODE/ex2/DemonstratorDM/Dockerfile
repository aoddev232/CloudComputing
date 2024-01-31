# Dockerfile for the Demonstrator Data Mining role
FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY demonstrator_dm.py /
RUN pip install pika
CMD ["sh", "-c", "sleep 60 && python3 demonstrator_dm.py"]