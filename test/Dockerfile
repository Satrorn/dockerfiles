# 指定构建的基础镜像
FROM alpine:latest AS builder

# ***** 安装依赖 *****
RUN apk add --no-cache bash git curl wget bash zip

# 克隆源码运行安装
RUN git clone --progress https://github.com/CareyWang/sub-web sub-web
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue

# 指定创建的基础镜像
FROM alpine:latest
COPY --from=builder /sub-web /app
WORKDIR /app
RUN yarn install 

#EXPOSE 80 
#CMD [ "nginx", "-g", "daemon off;" ]
