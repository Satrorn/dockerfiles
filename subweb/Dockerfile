FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.5

RUN apk add --no-cache bash git curl

WORKDIR /app

RUN set -eux \
    && mkdir -p /app/sub-web \
    && git clone https://github.com/zhongfly/sub-web.git /app/sub-web
    
COPY conf/.env /app/sub-web/.env
COPY conf/Subconverter.vue /app/sub-web/src/views/Subconverter.vue

RUN set -eux \
    && cp -rf /app/sub-web/package.json /app \
    && yarn install

FROM dependencies AS build

WORKDIR /app

COPY /app/sub-web/* /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
