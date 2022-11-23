FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.2.3

RUN apk add --no-cache bash git py3-pip py3-tinydb

WORKDIR /data

RUN set -eux \
    && wget -O nightly-20221007.tar.gz "https://github.com/CzBiX/qb-web/archive/refs/tags/nightly-20221007.tar.gz" \
    && mkdir -p /data/temp/nightly \
    && tar xzf nightly-20221007.tar.gz -C /data/temp/nightly \
    && cp -rf /data/temp/nightly/* /data/webui \
    && rm -rf nightly-20221007.tar.gz \
    && rm -rf /data/temp/*

RUN set -eux \
    && mkdir -p /data/qb_dispatch \
    && git clone https://github.com/spartazhc/qb_dispatch /data/qb_dispatch \
    && pip3 install -r /data/qb_dispatch/requirement.txt

COPY diy.sh /data/diy/diy.sh
COPY config.ini /data/qb_dispatch/config.ini

VOLUME ["/data"]
ENTRYPOINT ["/init"]
