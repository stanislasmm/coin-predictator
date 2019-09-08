# Version: 0.0.1
FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y 
RUN apt-get update && apt-get install -y \
	locales \
	locales-all \
	software-properties-common

RUN locale-gen en_US.UTF-8 && export LANG=en_US.UTF-8 && export LC_ALL=en_US.UTF-8

RUN apt-get install -y tzdata curl vim git pv wget g++
RUN mkdir -p /usr/local/share/tmp
RUN mkdir -p /usr/local/var/log/
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python2.7
RUN apt-get install -y python3.6
RUN apt-get install -y python3.6-dev
RUN apt-get install -y python3-distutils
RUN apt-get install -y gettext-base
RUN apt-get install -y python-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y libpq-dev

# pip install
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py 'pip<10'


# some pb with the default virtualenv install not working, had to force upgrade
# create the venv
RUN pip3.6 install --upgrade virtualenv

RUN pip install httpie

# Computation backend initialization
RUN mkdir -p /app
RUN cd /app && virtualenv -p python3.6 /venv --prompt="(VENV)"
ADD requirements.txt /app/requirements.txt
RUN /bin/bash -c "cd /app/ && source /venv/bin/activate && pip3.6 install -r requirements.txt"
RUN mkdir -p /app/src
COPY src/ /app/src

WORKDIR /app
RUN mkdir -p xp_logs

CMD bash