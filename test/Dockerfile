FROM node:16-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

RUN apk add --no-cache bash git curl wget jq make zip unzip

WORKDIR /app

# 克隆源码运行安装
RUN git clone https://github.com/CareyWang/sub-web.git /sub-web
   
#COPY conf/.env /sub-web/.env
#COPY conf/Subconverter.vue /sub-web/src/views/Subconverter.vue

# ---- Dependencies ----
FROM node:16-alpine AS dependencies
WORKDIR /app
COPY /sub-web/package.json ./
RUN yarn install

# ---- Build ----
FROM dependencies AS build
WORKDIR /app
COPY . /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]