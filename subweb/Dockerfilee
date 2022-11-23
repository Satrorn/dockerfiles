FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.2.0

RUN apk add --no-cache bash git curl zip

WORKDIR /data

RUN set -eux \
    && mkdir -p /data \
    && mkdir -p /data/zh \
    && git clone https://github.com/satrorn/dockerfiles /data/zh \
    && cp -rf /data/zh/* /data
    
COPY conf/.env /data/.env
COPY conf/Subconverter.vue /data/src/views/Subconverter.vue

WORKDIR /data
COPY /data/package.json ./data
RUN yarn install

FROM dependencies AS build
WORKDIR /app
COPY . /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
