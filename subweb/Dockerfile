FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3

# 克隆源码运行安装
RUN git clone https://github.com/CareyWang/sub-web.git /sub-web

# 拷贝配置文件
COPY conf/.env /sub-web/.env
COPY conf/Subconverter.vue /sub-web/src/views/Subconverter.vue

WORKDIR /app
RUN npm install
RUN npm run build

FROM danxiaonuo/nginx:latest
WORKDIR /www
COPY --from=build /app/dist /www

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
