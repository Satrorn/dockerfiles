FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3

# ***** 安装依赖 *****
RUN apk add --no-cache bash git py3-pip py3-tinydb

WORKDIR /data

# ***** 复制文件 *****
RUN git clone https://github.com/spartazhc/qb_dispatch.git /data/qb_dispatch
#COPY qb_dispatch /data/qb_dispatch
COPY ui /data/ui
COPY diy.sh /data/diy/diy.sh
#COPY requirement.txt /data
COPY . /data

RUN pip3 install -r /data/qb_dispatch/requirement.txt

VOLUME ["/data"]
ENTRYPOINT ["/init"]
