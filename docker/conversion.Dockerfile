FROM python:3.7

ENV HOME /home/col

WORKDIR /home/col

RUN apt-get update -y && apt-get install -y bash-completion python3-pip python3-dev unzip default-mysql-client

RUN pip install --upgrade pip && \
    pip install mysqlclient mysql mysql-connector-python
