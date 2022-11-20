FROM tindy2013/subconverter
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.7.2

WORKDIR /base
RUN apk add tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

COPY conf/base/all_base.tpl /base/base
COPY conf/base/Parents.yml /base
COPY conf/config /base/config/
COPY conf/rules /base/rules/


EXPOSE 25500

WORKDIR /base

CMD subconverter