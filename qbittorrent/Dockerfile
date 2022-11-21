FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

# ***** 安装依赖 *****
RUN set -eux && \
   # 修改源地址
   sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
   # 更新源地址并更新系统软件
   apk update && apk upgrade
   # 安装依赖包
   apk add --update git && apk add --update py3-pip && apk add --update py3-tinydb

RUN git clone https://github.com/spartazhc/qb_dispatch /qb_dispatch
COPY ui /data/ui
COPY diy.sh /data/diy/diy.sh
COPY start.sh /data/qb_dispatch/start.sh
CMD [ "sh", "-c", "/data/qb_dispatch/start.sh" ]
VOLUME ["/qb_dispatch"]
