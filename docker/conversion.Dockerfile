FROM python:3.7

ENV HOME /root

WORKDIR /home/col/bin

RUN apt-get update -y && apt-get install -y bash-completion python3-pip python3-dev unzip default-mysql-client

RUN pip install --upgrade pip && \
    pip install mysqlclient mysql mysql-connector-python pandas
    
