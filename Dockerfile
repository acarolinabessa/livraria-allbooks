FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000