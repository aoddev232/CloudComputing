# Dockerfile for the student role
FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY student.py /
RUN pip install pika
CMD ["sh", "-c", "sleep 60 && python3 student.py"]