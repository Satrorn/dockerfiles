FROM node:16-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

WORKDIR /app

# 克隆源码运行安装
RUN git clone https://github.com/CareyWang/sub-web.git /app
   
#COPY conf/.env /sub-web/.env
#COPY conf/Subconverter.vue /sub-web/src/views/Subconverter.vue
