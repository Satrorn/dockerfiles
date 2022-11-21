FROM satrorn/zh
LABEL maintainer="Satrorn <satrorn@gmail.com>"

ENV VERSION 0.1.2

WORKDIR /app
COPY conf/.env /app
COPY conf/Subconverter.vue /app/src/views
RUN cd /app && npm install && npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
