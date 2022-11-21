FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

# ***** 安装依赖 *****
RUN apk add --no-cache bash git py3-pip py3-tinydb

# ***** 复制文件 *****
RUN git clone https://github.com/spartazhc/qb_dispatch /qb_dispatch
COPY ui /data/ui
COPY diy.sh /data/diy/diy.sh
COPY start.sh /data/qb_dispatch/start.sh

CMD [ "sh", "-c", "/data/qb_dispatch/start.sh" ]
VOLUME ["/qb_dispatch"]
