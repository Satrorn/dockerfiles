FROM tindy2013/subconverter
LABEL maintainer="Satrorn <satrorn@gmaill.com>"

ENV VERSION 0.7.2

WORKDIR /base
RUN apk add tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

COPY groups.txt rulesets.txt /base/snippets/
COPY pref.yml /base
COPY conf/base/all_base.tpl /subconverter/base/all_base.tpl
COPY conf/base/Parents.yml /subconverter/base/Parents.yml
COPY conf/rules /subconverter/rules
COPY conf/config /subconverter/config

EXPOSE 25500

WORKDIR /base

CMD subconverter
