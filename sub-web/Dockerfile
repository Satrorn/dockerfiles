FROM alpine:latest as base
LABEL maintainer="satrorn <satrorn@gmail.com>"

RUN apk add --update git
RUN git clone https://github.com/satrorn/sub /sub-web
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue

WORKDIR /sub-web
RUN npm install
RUN npm run build

FROM nginx:1.16-alpine
COPY --from=build /sub-web/dist /usr/share/nginx/html
COPY . /sub-web

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
