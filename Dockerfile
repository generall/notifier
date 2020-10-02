FROM python:3.7-alpine

WORKDIR /usr/src/app

ENV FLASK_APP=server.py

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD "python -m flask run"