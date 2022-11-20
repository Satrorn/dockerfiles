FROM tindy2013/subconverter
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.7.2

WORKDIR /base

COPY conf/base/all_base.tpl /base/base
COPY conf/base/Parents.yml /base/base
COPY conf/config /base/config/
COPY conf/rules /base/rules/


EXPOSE 25500

WORKDIR /base

CMD subconverter
