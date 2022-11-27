FROM node:14-alpine AS build
LABEL maintainer="Satrorn <satrorn@gmail.com>"
ENV VERSION 0.1.1

RUN set -eux \
    && apk add --no-cache git \
    && git clone https://github.com/CareyWang/sub-web.git /app \
    && cp conf/.env /app/.env \
    && cp conf/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app

RUN set -eux \
    && yarn install \
    && yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]