FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3

WORKDIR /app
RUN git clone https://github.com/CareyWang/sub-web.git /app/sub-web

COPY conf/.env /app/sub-web/.env
COPY conf/Subconverter.vue /app/sub-web/src/views/Subconverter.vue

COPY /app/sub-web/package.json /app
RUN yarn install

FROM dependencies AS build
WORKDIR /app
COPY /app/sub-web/. /app
RUN rm -rf /app/sub-web
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
