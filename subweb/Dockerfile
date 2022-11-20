FROM node:14-alpine AS build
LABEL maintainer="Satrorn <satrorn@gmail.com>"

RUN apk add --update git
RUN git clone https://github.com/CareyWang/sub-web app
COPY conf/.env /app
COPY start.sh /app
COPY conf/Subconverter.vue /app/src/views
RUN cd /app && npm install && npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "sh", "-c", "/app/start.sh" ]