FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

# ***** 安装依赖 *****
RUN apk add --no-cache bash git py3-pip py3-tinydb

WORKDIR /data

# ***** 复制文件 *****
COPY qb_dispatch /data/qb_dispatch
COPY ui /data/ui
COPY diy.sh /data/diy/diy.sh
ADD qb_dispatch/requirements.txt /data/requirements.txt

RUN pip3 install -r requirements.txt

VOLUME ["/data"]
ENTRYPOINT ["/init"]
