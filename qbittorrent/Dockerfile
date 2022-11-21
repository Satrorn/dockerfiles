FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

# ***** 安装依赖 *****
RUN apk add --no-cache bash git py3-pip py3-tinydb

# ***** 复制文件 *****
RUN git clone https://github.com/spartazhc/qb_dispatch /qb_dispatch
#WORKDIR /qb_dispatch
#RUN pip3 install -r requirements.txt

#WORKDIR /data
COPY ui /data/ui
COPY diy.sh /data/diy/diy.sh
#RUN pip3 install -r /data/qb_dispatch/requirements.txt

VOLUME ["/data"]
ENTRYPOINT ["/init"]
