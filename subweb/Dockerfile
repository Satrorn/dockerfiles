FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3

# 克隆源码运行安装
ADD . .
RUN git clone https://github.com/CareyWang/sub-web.git /app

# 拷贝配置文件
COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
