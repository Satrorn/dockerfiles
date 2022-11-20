FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

WORKDIR /data

RUN apk update && \
    apk add --update git && \
    apk add --update py3-pip && \
    apk add --update py3-tinydb

COPY qb_dispatch/ ./qb_dispatch/
COPY ui/ ./ui/
COPY diy.sh ./
COPY qb_dispatch/requirement.txt ./
RUN ./install.sh

VOLUME ["/data"]
ENTRYPOINT ["/init"]
