FROM alpine:latest as base
LABEL maintainer="satrorn <satrorn@gmail.com>"

RUN apk add --update git
RUN git clone https://github.com/zhongfly/sub-web/ /app
COPY conf/sub-web/.env /app/.env
COPY conf/sub-web/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /sub-web/dist /usr/share/nginx/html
COPY . /app

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
