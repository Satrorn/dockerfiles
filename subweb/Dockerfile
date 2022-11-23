FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.6

RUN apk add --no-cache bash git curl wget jq make zip unzip

WORKDIR /app

RUN set -eux \
    && git clone https://github.com/zhongfly/sub-web /app
   
COPY conf/.env /app/sub-web/.env
COPY conf/Subconverter.vue /app/sub-web/src/views/Subconverter.vue
 
WORKDIR /app 
COPY --from=builder /sub-web/package.json ./app 
RUN yarn install 

FROM dependencies AS build 
WORKDIR /app 
COPY --from=builder /sub-web/ ./app 
RUN yarn build 
  
FROM nginx:1.16-alpine 
COPY --from=build /app/dist /usr/share/nginx/html 
EXPOSE 80 
CMD [ "nginx", "-g", "daemon off;" ]
