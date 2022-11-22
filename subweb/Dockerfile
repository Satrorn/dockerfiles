FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.4

WORKDIR /app

RUN set -ex \
    && git clone --progress git clone https://github.com/satrorn/dockerfiles.git /app/dk \
    && mv /app/files/zh/* /app \
    && rm -rf /app/dk

RUN set -ex \
    && rm -rf /app/.env
    && cp conf/.env /app/.env
    && rm -rf /app/src/views/Subconverter.vue
    && cp conf/Subconverter.vue /app/src/views/Subconverter.vue
    && cd /app && npm install && npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]

