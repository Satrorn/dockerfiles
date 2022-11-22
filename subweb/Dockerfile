FROM satrorn/zh
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3

RUN set -ex \
    && git clone --progress git clone https://github.com/satrorn/dockerfiles.git /app/dk \
    && mv /app/files/zh /app \
    && rm -rf /app/dk

RUN set -ex \
    && rm -rf /app/.env
    && cp conf/.env /app/.env
    && rm -rf /app/src/views/Subconverter.vue
    && cp conf/Subconverter.vue /app/src/views/Subconverter.vue

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
