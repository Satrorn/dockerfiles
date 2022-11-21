FROM satrorn/zh
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

COPY conf/.env /app
COPY conf/Subconverter.vue /app/src/views

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
