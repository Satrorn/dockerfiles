# ---- Dependencies ----
FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.9

RUN apk add --no-cache bash git curl
WORKDIR /app
RUN set -eux \
    && mkdir -p /all \
    && git clone https://github.com/satrorn/dockerfiles /all \
    && mkdir -p /zz \
    && cp -rf /all/zh /zz \
    && rm -rf /all
    
COPY conf/.env /zz/.env
COPY conf/Subconverter.vue /zz/src/views/Subconverter.vue

WORKDIR /app
COPY /zz/package.json ./
RUN yarn install

# ---- Build ----
FROM dependencies AS build
WORKDIR /app
COPY /zz/. /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
