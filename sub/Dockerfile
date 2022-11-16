FROM danxiaonuo/subweb
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue
RUN yarn install

# ---- Build ----
FROM dependencies AS build
WORKDIR /app
COPY . /app
RUN yarn build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
