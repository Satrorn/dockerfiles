# 指定构建的基础镜像
FROM node:14-alpine AS builder

# 作者描述信息
LABEL maintainer="Satrorn <satrorn@gmail.com>"

# 版本号
ENV VERSION 0.2.0

# 工作目录
WORKDIR /app

RUN set -eux && \
   # 修改源地址
   sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
   # 更新源地址并更新系统软件
   apk update && apk upgrade && \
   # 安装依赖包
   apk add --no-cache git curl wget bash

# 克隆源码运行安装
RUN set -eux \
    && git clone https://github.com/CareyWang/sub-web.git /app

# 拷贝配置文件
COPY conf/.env /app/.env
COPY conf/Subconverter.vue /app/src/views/Subconverter.vue

# 静态页面运行安装
RUN yarn install
RUN yarn build

# 指定创建的基础镜像
FROM nginx:1.16-alpine

# 拷贝资源文件
COPY --from=builder /app/dist usr/share/nginx/html
#COPY --from=builder /app /app

# 启动命令
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
