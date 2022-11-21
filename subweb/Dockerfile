FROM nevinee/qbittorrent
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

WORKDIR /sub-web
COPY conf/.env /sub-web/.env
COPY conf/Subconverter.vue /sub-web/src/views/Subconverter.vue

EXPOSE 80
CMD [ "sh", "-c", "/app/start.sh" ]
