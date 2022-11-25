FROM node:lts-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

WORKDIR /app

RUN set -eux \
    && git clone --progress https://github.com/CareyWang/sub-web.git /sub-web
