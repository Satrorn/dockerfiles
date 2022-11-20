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
COPY diy.sh /data/diy/diy.sh
COPY start.sh /data
COPY qb_dispatch/requirement.txt /data
CMD [ "sh", "-c", "/data/start.sh" ]

VOLUME ["/data"]
ENTRYPOINT ["/init"]
