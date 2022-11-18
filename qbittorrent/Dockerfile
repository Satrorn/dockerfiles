# 在qb外部程序中填dl-finish "%I" "%F" "%L" "%N"
# diy.sh设置文件
# python3 /data/qb_dispatch/qb_dispatch.py -f "$2" -c "$3" -n "$4"

# 指定构建的基础镜像
FROM nevinee/qbittorrent:latest

# ***** 安装依赖 *****
RUN set -eux \
    && git clone --progress https://github.com/spartazhc/qb_dispatch.git /data/qb_dispatch

RUN apk add --no-cache \
       py3-pip \
       py3-tinydb

# 拷贝配置文件	
COPY conf/config.ini /data/qb_dispatch/config.ini
COPY conf/diy.sh /data/diy/diy.sh
COPY conf/ui /data/ui

WORKDIR /data/qb_dispatch

RUN python3 -m pip install -r requirement.txt
