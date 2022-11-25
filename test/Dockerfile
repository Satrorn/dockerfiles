FROM node:16-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

RUN apk add --no-cache bash git curl wget jq make zip unzip

WORKDIR /app

# 克隆源码运行安装
RUN git clone https://github.com/CareyWang/sub-web.git /
   
#COPY conf/.env /sub-web/.env
#COPY conf/Subconverter.vue /sub-web/src/views/Subconverter.vue
