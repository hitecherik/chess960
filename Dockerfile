FROM python:3-alpine3.11

WORKDIR /app
RUN pip3 install flask
COPY . .

CMD python3 server.py
