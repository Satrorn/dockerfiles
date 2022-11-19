##########################################
#            设置公共的变量               #
##########################################
# 指定构建的基础镜像
FROM node:lts-alpine AS dependencies

# 作者描述信息
MAINTAINER danxiaonuo
# 时区设置
ARG TZ=Asia/Shanghai
ENV TZ=$TZ
# 语言设置
ARG LANG=C.UTF-8
ENV LANG=$LANG

# 镜像变量
ARG DOCKER_IMAGE=danxiaonuo/sub-web
ENV DOCKER_IMAGE=$DOCKER_IMAGE
ARG DOCKER_IMAGE_OS=node
ENV DOCKER_IMAGE_OS=$DOCKER_IMAGE_OS
ARG DOCKER_IMAGE_TAG=lts-alpine
ENV DOCKER_IMAGE_TAG=$DOCKER_IMAGE_TAG

ARG PKG_DEPS="\
      zsh \
      bash \
      bind-tools \
      iproute2 \
      git \
      vim \
      tzdata \
      curl \
      wget \
      lsof \
      zip \
      unzip \
      ca-certificates"
ENV PKG_DEPS=$PKG_DEPS

# ***** 安装依赖 *****
RUN set -eux && \
   # 修改源地址
   sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
   # 更新源地址并更新系统软件
   apk update && apk upgrade && \
   # 安装依赖包
   apk add --no-cache --clean-protected $PKG_DEPS && \
   rm -rf /var/cache/apk/* && \
   # 更新时区
   ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime && \
   # 更新时间
   echo ${TZ} > /etc/timezone && \
   # 更改为zsh
   sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true && \
   sed -i -e "s/bin\/ash/bin\/zsh/" /etc/passwd && \
   sed -i -e 's/mouse=/mouse-=/g' /usr/share/vim/vim*/defaults.vim && \
   /bin/zsh

# 克隆源码运行安装
RUN set -eux \
    && git clone --progress https://github.com/CareyWang/sub-web.git /sub-web

# 拷贝配置文件	
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue

# 工作目录
WORKDIR /app

RUN set -eux \
    && cp conf/sub-web/package.json /app \
    && yarn install

# ##############################################################################
    
##########################################
#            构建运行环境                 #
##########################################
FROM dependencies AS build
WORKDIR /app
RUN set -eux \
    && cp -rf conf/sub-web/. /app \
    && yarn build

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
COPY conf/sub-web/vhost/default.conf /data/nginx/conf/vhost/default.conf

# 容器信号处理
STOPSIGNAL SIGQUIT

# 启动命令
CMD ["nginx", "-g", "daemon off;"]
