FROM node:12-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3

RUN git clone https://github.com/CareyWang/sub-web /sub-web

COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app
COPY /sub-web/package.json /app
RUN yarn install

FROM dependencies AS build
WORKDIR /app
COPY . /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
