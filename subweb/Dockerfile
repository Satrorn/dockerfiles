FROM alpine:latest as base
LABEL maintainer="satrorn <satrorn@gmail.com>"

RUN apk add --update git
RUN git clone https://github.com/satrorn/sub-web /app
COPY conf/sub-web/.env /app
COPY conf/sub-web/Subconverter.vue /app/src/views

WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app

EXPOSE 80
CMD [ "sh", "-c", "/app/start.sh" ]
