FROM python:3.8
FROM python:3.7-alpine

WORKDIR /app
WORKDIR /src/app/

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY ./requirements.txt .

COPY . /app
RUN ["pip", "install", "-r", "./requirements.txt"]

CMD ["python", "/app/src/app.py"]
COPY . .

RUN addgroup -S projects && adduser -S -H projects -G projects
RUN chown -R projects:projects /src/app
USER projects
