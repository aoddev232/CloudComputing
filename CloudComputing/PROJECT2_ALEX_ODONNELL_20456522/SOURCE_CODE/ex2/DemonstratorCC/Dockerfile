# Dockerfile for the Demonstrator Cloud Computing role
FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY demonstrator_cc.py /
RUN pip install pika
CMD ["sh", "-c", "sleep 60 && python3 demonstrator_cc.py"]