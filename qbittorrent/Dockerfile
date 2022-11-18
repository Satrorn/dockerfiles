# 在qb外部程序中填dl-finish "%I" "%F" "%L" "%N"
# diy.sh设置文件
# python3 /data/qb_dispatch/qb_dispatch.py -f "$2" -c "$3" -n "$4"

# 指定构建的基础镜像
FROM nevinee/qbittorrent:latest

# ***** 安装依赖 *****
RUN apk add --no-cache \
       py3-pip \
       py3-tinydb

WORKDIR /qb_dispatch
RUN git clone --progress https://github.com/spartazhc/qb_dispatch.git /qb_dispatch	
COPY conf/config.ini /qb_dispatch/config.ini
RUN python3 -m pip install -r requirement.txt

WORKDIR /diy
COPY conf/diy.sh diy/diy.sh

EXPOSE 9092
CMD ["nginx","-g",""daemon off;]
