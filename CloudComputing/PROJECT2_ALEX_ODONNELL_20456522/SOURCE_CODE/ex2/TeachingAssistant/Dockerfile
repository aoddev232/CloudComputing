# Dockerfile for the student role
FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY teaching_assistant.py /
RUN pip install pika
CMD ["sh", "-c", "sleep 60 && python3 teaching_assistant.py"]