FROM node:14-alpine AS builder
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3
WORKDIR /app

RUN apk add --no-cache git
RUN git clone https://github.com/zhongfly/sub-web /app
COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

RUN yarn install
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=builder /app/dist usr/share/nginx/html
#COPY --from=builder /app /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
