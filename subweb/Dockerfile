FROM node:14-alpine AS build
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

WORKDIR /app
RUN git clone https://github.com/Satrorn/dockerfiles /app/base
COPY --from=0 /app/base/zh /app

COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
