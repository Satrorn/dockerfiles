FROM node:14-alpine AS build
LABEL maintainer="Satrorn <satrorn@gmail.com>"

RUN apk add --update git
RUN git clone https://github.com/satrorn/zh app
COPY conf/.env /app
COPY start.sh /app
COPY conf/Subconverter.vue /app/src/views

WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "sh", "-c", "/app/start.sh" ]
