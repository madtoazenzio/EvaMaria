FROM python:3.9-slim-buster

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

RUN mkdir /movie-world
WORKDIR /movie-world
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"] && python3 main.py
