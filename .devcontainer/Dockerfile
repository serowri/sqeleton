FROM ubuntu:22.04

WORKDIR /workspace/sqeleton

RUN apt-get update && apt-get install -y \
    apt-get install python3 \
    apt-get install python3-pip \
    && apt-get clean

RUN pip install numpy

COPY .. .
