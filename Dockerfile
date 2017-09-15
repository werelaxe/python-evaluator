FROM ubuntu:16.04

LABEL maintainer="werelaxe"

RUN apt-get update && apt-get install python3 -y
RUN apt-get install python3-setuptools -y
RUN apt-get install git -y
RUN easy_install3 pip
RUN pip3 install flask
RUN mkdir /home/evaluator

COPY . /home/evaluator

ENTRYPOINT ["python3", "/home/evaluator/main.py"]

