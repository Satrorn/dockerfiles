FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.2.1

# ***** 安装依赖 *****
RUN apk add --no-cache bash git py3-pip py3-tinydb

WORKDIR /data

# ***** 汉化文件 *****
RUN wget --no-check-certificate -P /data https://github.com/CzBiX/qb-web/archive/refs/tags/nightly-20221007.tar.gz -O /data/nightly-20221007.tar.gz &&  \
    tar xzf nightly-20221007.tar.gz &&  \
    rm -rf nightly-20221007.tar.gz &&

# ***** 复制文件 *****
RUN git clone https://github.com/spartazhc/qb_dispatch.git /data/qb_dispatch
COPY diy.sh /data/diy/diy.sh
COPY . /data

RUN pip3 install -r /data/qb_dispatch/requirement.txt

VOLUME ["/data"]
ENTRYPOINT ["/init"]