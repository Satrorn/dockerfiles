FROM tindy2013/subconverter
LABEL maintainer="Satrorn <satrorn@gmaill.com>"

ENV VERSION 0.7.2

WORKDIR /base
RUN apk add tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

COPY conf/ /base/config
COPY pref.yml /base
COPY groups.txt rulesets.txt /base/snippets/
COPY all_base.tpl Parents.yml /base/base/
COPY Country.list Line.list /base/rules/ACL4SSR/

EXPOSE 25500

WORKDIR /base

CMD subconverter
