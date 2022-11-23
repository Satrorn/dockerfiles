# ---- Dependencies ----
FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.9

RUN apk add --no-cache bash git curl
WORKDIR /app
RUN set -eux \
    && mkdir -p /all \
    && git clone https://github.com/satrorn/dockerfiles /all \
    
COPY conf/.env /all/zh/.env
COPY conf/Subconverter.vue /all/zh/src/views/Subconverter.vue

WORKDIR /app
COPY /all/zh/package.json ./
RUN yarn install

# ---- Build ----
FROM dependencies AS build
WORKDIR /app
COPY /all/zh/. /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
