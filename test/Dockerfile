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
    && git clone --progress https://github.com/CareyWang/sub-web.git /sub-web \
    && cp -rf /sub-web/* /app

WORKDIR /app
RUN yarn install

# ---- Build ----
FROM dependencies AS build
WORKDIR /app
COPY /app/* /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
