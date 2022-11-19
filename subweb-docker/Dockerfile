# 指定创建的基础镜像
FROM node:14-alpine AS build
LABEL maintainer="satrorn <satrorn@gmail.com>"

RUN apk add --update git
RUN git clone https://github.com/CareyWang/sub-web /app
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue

WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app

EXPOSE 80
CMD [ "sh", "-c", "/app/start.sh" ]
