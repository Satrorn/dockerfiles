# ---- Dependencies ----
FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.7

RUN apk add --no-cache bash git curl

RUN set -eux \
    && mkdir -p /app \
    && mkdir -p /app/zh \
    && git clone https://github.com/satrorn/dockerfiles/zh /app/zh \
    && cp /app/zh /app
    
COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app
COPY package.json ./
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
