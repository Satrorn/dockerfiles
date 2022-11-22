FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.5

WORKDIR /app

RUN git clone https://github.com/satrorn/dockerfiles /app/dk
RUN mv /app/dk/zh/* /app
RUN rm -rf /app/dk

RUN rm -rf /app/.env
COPY conf/.env /app/.env
RUN rm -rf /app/src/views/Subconverter.vue
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue
RUN cd /app && npm install && npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]

