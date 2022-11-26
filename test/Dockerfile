FROM node:14-alpine AS build

RUN apk add --no-cache bash git curl wget bash zip

RUN git clone --progress https://github.com/CareyWang/sub-web.git /ap
COPY conf/sub-web/.env /app/.env
COPY conf/sub-web/Subconverter.vue /app/src/views/Subconverter.vue

WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine 
COPY --from=builder /app/dist /usr/share/nginx/html 
EXPOSE 80 
CMD [ "nginx", "-g", "daemon off;" ]
