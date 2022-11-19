FROM node:14-alpine AS build
LABEL maintainer="satrorn <satrorn@gmail.com>"

RUN apk update && \
    apk add --update git && \
    apk add --update py3-pip && \
    apk add --update py3-tinydb

RUN git clone https://github.com/satrorn/qbittorrent /app
RUN git clone https://github.com/spartazhc/qb_dispatch /app
COPY conf/diy.sh diy/diy.sh

WORKDIR /qb_dispatch
COPY conf/config.ini /qb_dispatch/config.ini
RUN python3 -m pip install -r requirement.txt

WORKDIR /data
VOLUME ["/data"]
ENTRYPOINT ["/init"]
