FROM node:lts-alpine AS dependencies

LABEL maintainer="Satrorn <satrorn@gmail.com>"
ENV VERSION 0.1.7

# ***** 安装依赖 *****
RUN set -eux && \
   # 修改源地址
   sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
   # 更新源地址并更新系统软件
   apk update && apk upgrade && \
   # 安装依赖包
   apk add --no-cache --clean-protected git curl wget bash

# 克隆源码运行安装
RUN set -eux \
    && git clone --progress https://github.com/CareyWang/sub-web.git /sub-web

# 拷贝配置文件	
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue


# ##############################################################################
    
##########################################
#            构建运行环境                 #
##########################################
FROM dependencies AS build
WORKDIR /app
RUN set -eux \
    && cp -rf /sub-web/* /app
    
RUN yarn install
RUN yarn build

# ##############################################################################


##########################################
#         构建基础镜像                    #
##########################################
# 
# 指定创建的基础镜像
FROM danxiaonuo/nginx:latest

# 工作目录
WORKDIR /www

# 拷贝资源文件
COPY --from=build /app/dist /www

# 容器信号处理
STOPSIGNAL SIGQUIT

# 启动命令
CMD ["nginx", "-g", "daemon off;"]
