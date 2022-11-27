FROM node:16-alpine AS dependencies

RUN apk add --no-cache git

RUN git clone https://github.com/CareyWang/sub-web.git /app
COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app
RUN yarn install
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=builder /app/dist usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
