FROM node:14-alpine AS build
LABEL maintainer="satrorn <satrorn@gmail.com>"

RUN apk update && \
    apk add --update git && \
    apk add --update py3-pip && \
    apk add --update py3-tinydb

RUN git clone https://github.com/satrorn/qbittorrent /app
COPY requirements.txt /tmp/requirements.txt
RUN ["pip", "install", "-r", "/tmp/requirements.txt"]

RUN git clone https://github.com/spartazhc/qb_dispatch.git /data/qb_dispatch
COPY conf/diy.sh /data/diy/diy.sh
COPY conf/config.ini /data/qb_dispatch/config.ini

WORKDIR /data
VOLUME ["/data"]
ENTRYPOINT ["/init"]
