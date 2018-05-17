FROM ubuntu:xenial

RUN apt-get update && apt-get upgrade

RUN apt-get install -y --no-install-recommends python3 python3-dev python3-pip python3-setuptools

RUN pip3 install --upgrade pip
RUN pip3 install tweepy && \
    pip3 install praw

ADD shitpost.py /home/shitpost.py

ADD shitcron /etc/cron.d/shitcron

RUN chmod 0644 /etc/cron.d/shitcron


