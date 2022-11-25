FROM node:alpine
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

RUN apk add --no-cache bash git curl wget jq make zip unzip

WORKDIR /app

# 克隆源码运行安装
RUN set -eux \
    && git clone --progress https://github.com/CareyWang/sub-web.git /app/sub-web
   
COPY conf/.env /app/sub-web/.env
COPY conf/Subconverter.vue /app/sub-web/src/views/Subconverter.vue
 
WORKDIR /app 
COPY /app/sub-web/package.json ./app 
RUN yarn install

FROM dependencies AS build
WORKDIR /app
COPY /app/sub-web/. /app
RUN yarn build


FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]