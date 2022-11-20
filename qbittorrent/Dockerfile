FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

WORKDIR /data

RUN apk update && \
    apk add --update git && \
    apk add --update py3-pip && \
    apk add --update py3-tinydb

RUN git clone https://github.com/spartazhc/qb_dispatch qb_dispatch
COPY ui/ /data/ui/
COPY diy.sh /data/diy/diy.sh
COPY start.sh /data/qb_dispatch/start.sh
CMD [ "sh", "-c", "/data/qb_dispatch/start.sh" ]

WORKDIR /data
VOLUME ["/data"]
ENTRYPOINT ["/init"]
