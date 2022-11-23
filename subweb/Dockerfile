# ---- Dependencies ----
FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.9

RUN apk add --no-cache bash git curl
WORKDIR /app
RUN set -eux \
    && mkdir -p /app/all \
    && git clone https://github.com/satrorn/dockerfiles /app/all \
    && mkdir -p /app/zz \
    && cp /app/all/zh /app/zz \
    
COPY conf/.env /app/zz/.env
COPY conf/Subconverter.vue /app/zz/src/views/Subconverter.vue

WORKDIR /app
COPY /app/zz/package.json ./app
RUN yarn install

# ---- Build ----
FROM dependencies AS build
WORKDIR /app
COPY /app/zz/. /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
