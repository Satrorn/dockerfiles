# ---- Dependencies ----
FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.9

RUN apk add --no-cache bash git curl

RUN set -eux \
    && mkdir -p /app/zh \
    && git clone https://github.com/satrorn/dockerfiles/zh /app/zh \
    
COPY conf/.env /app/zh/.env
COPY conf/Subconverter.vue /app/zh/src/views/Subconverter.vue

WORKDIR /zh
COPY package.json ./
RUN yarn install

# ---- Build ----
FROM dependencies AS build
WORKDIR /zh
COPY . /zh
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /zh/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
