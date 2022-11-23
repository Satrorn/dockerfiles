FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

RUN apk add --no-cache bash git curl

WORKDIR /base

RUN set -eux \
    && mkdir -p /base/sub \
    && git clone https://github.com/zhongfly/sub-web /base/sub
    
COPY conf/.env /base/sub/.env
COPY conf/Subconverter.vue /base/sub/src/views/Subconverter.vue

# ---- Dependencies ---- 
 FROM node:16-alpine AS dependencies 
 WORKDIR /app 
 COPY /base/sub/package.json ./ 
 RUN yarn install 
  
 # ---- Build ---- 
 FROM dependencies AS build 
 WORKDIR /app 
 COPY /base/sub/. /app 
 RUN yarn build 
  
 FROM nginx:1.16-alpine 
 COPY --from=build /app/dist /usr/share/nginx/html 
 EXPOSE 80 
 CMD [ "nginx", "-g", "daemon off;" ]
