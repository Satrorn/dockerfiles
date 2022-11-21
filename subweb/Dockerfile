FROM node:14-alpine AS build
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

WORKDIR /base
RUN git clone https://github.com/Satrorn/dockerfiles /base

WORKDIR /app
COPY --from=0 /base/zh /app
COPY /base/zh /app
COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
