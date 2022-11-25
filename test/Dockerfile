# 指定构建的基础镜像
FROM alpine:latest AS builder

# ***** 安装依赖 *****
RUN apk add --no-cache bash git curl wget bash zip

# 克隆源码运行安装
RUN git clone --progress https://github.com/CareyWang/sub-web apk

# 指定创建的基础镜像
FROM alpine:latest
COPY --from=builder /apk /app
RUN cd /app && npm install && npm run build

FROM nginx:1.16-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY . /app
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
