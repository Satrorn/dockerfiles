FROM node:lts-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"
ENV VERSION 0.1.6

# ***** 安装依赖 *****
RUN set -eux && \
   # 修改源地址
   sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
   # 更新源地址并更新系统软件
   apk update && apk upgrade && \
   # 安装依赖包
   apk add --no-cache --clean-protected git curl wget bash

# 克隆源码运行安装
RUN set -eux \
    && git clone --progress https://github.com/CareyWang/sub-web.git /sub-web

# 拷贝配置文件	
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue

# 工作目录
WORKDIR /app

RUN set -eux \
    && cp -rf /sub-web/* /app \
    && yarn install
