FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

WORKDIR /data

RUN apk update && \
    apk add --update git && \
    apk add --update py3-pip && \
    apk add --update py3-tinydb

COPY qb_dispatch/ /data/qb_dispatch/
COPY ui/ /data/ui/
COPY diy.sh /data/diy.sh
COPY requirements.txt /data/requirements.txt
RUN ["pip", "install", "-r", "/data/requirements.txt"]

VOLUME ["/data"]
ENTRYPOINT ["/init"]
