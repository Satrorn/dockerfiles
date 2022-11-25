FROM node:lts-alpine AS dependencies

LABEL maintainer="Satrorn <satrorn@gmail.com>"
ENV VERSION 0.1.7

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
    && git clone --progress https://github.com/CareyWang/sub-web /app \
    && cd /app \
    && npm install \
    && npm run build

FROM nginx:1.16-alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
