# Dockerfile for the Module Coordinator role
FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY module_coordinator.py /
RUN pip install pika
CMD ["sh", "-c", "sleep 60 && python3 module_coordinator.py"]