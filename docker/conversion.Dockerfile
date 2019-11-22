FROM python:3.7

ENV HOME /home/col
WORKDIR /home/col

# Install software dependencies
RUN apt-get update -y && apt-get install -y python3-pip python3-dev

# Install python dependencies
RUN pip install --upgrade pip && \
    pip install mysql-connector-python requests pandas.io pandas && \
    pip install --upgrade git+git://github.com/gdower/coldpy.git
