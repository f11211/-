FROM python:3.9-slim
WORKDIR /app
COPY api_server.py /app/
RUN pip install flask
EXPOSE 8080
CMD ["python", "api_server.py"]
