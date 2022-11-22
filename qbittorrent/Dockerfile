FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.2.2

# ***** °²×°ÒÀÀµ *****
RUN apk add --no-cache bash git py3-pip py3-tinydb

WORKDIR /data
ADD . .

RUN wget --no-check-certificate -P /data https://github.com/CzBiX/qb-web/archive/refs/tags/nightly-20221007.tar.gz -O /data/nightly-20221007.tar.gz
RUN tar xzf nightly-20221007.tar.gz
RUN rm -rf nightly-20221007.tar.gz


RUN git clone --progress git clone https://github.com/spartazhc/qb_dispatch.git /data/qb_dispatch
RUN cp -rf diy.sh /data/diy/diy.sh
RUN pip3 install -r /data/qb_dispatch/requirement.txt

VOLUME ["/data"]
ENTRYPOINT ["/init"]