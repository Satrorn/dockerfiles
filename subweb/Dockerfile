FROM satrorn/zh
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.3

COPY conf/.env /sub-web/.env
COPY conf/Subconverter.vue /sub-web/src/views/Subconverter.vue

WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
