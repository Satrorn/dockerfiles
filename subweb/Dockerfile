FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

RUN apk add --no-cache bash git curl

WORKDIR /sub-web

RUN set -eux \
    && mkdir -p /sub-web \
    && git clone https://github.com/zhongfly/sub-web /sub-web
    
COPY conf/.env /sub-web/.env
COPY conf/Subconverter.vue /sub-web/src/views/Subconverter.vue

RUN set -eux \
    && cp -rf /sub-web/package.json /app \
    && yarn install

FROM dependencies AS build

WORKDIR /app

COPY /sub-web/ /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
