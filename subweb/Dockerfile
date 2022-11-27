# ---- Dependencies ----
FROM node:16-alpine AS dependencies
LABEL maintainer="Satrorn <satrorn@gmaill.com>"
ENV VERSION 0.1.1

RUN apk add --no-cache git
RUN git clone https://github.com/CareyWang/sub-web.git /app
COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app
RUN yarn install

# ---- Build ----
FROM dependencies AS builder
WORKDIR /app
COPY --from=builder /app /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=builder /app/dist usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
