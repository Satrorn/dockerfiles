##########################################
#         构建可执行二进制文件             #
##########################################
# 指定构建的基础镜像
FROM golang:alpine AS builder

# 作者描述信息
MAINTAINER satrorn
# 时区设置
ARG TZ=Asia/Shanghai
ENV TZ=$TZ
# 语言设置
ARG LANG=C.UTF-8
ENV LANG=$LANG

# 版本号
ARG TAGS=v0.7.3
ENV TAGS=$TAGS

# 镜像变量
ARG DOCKER_IMAGE=satrorn/proxypool
ENV DOCKER_IMAGE=$DOCKER_IMAGE
ARG DOCKER_IMAGE_OS=golang
ENV DOCKER_IMAGE_OS=$DOCKER_IMAGE_OS
ARG DOCKER_IMAGE_TAG=alpine
ENV DOCKER_IMAGE_TAG=$DOCKER_IMAGE_TAG
ARG BUILD_DATE
ENV BUILD_DATE=$BUILD_DATE
ARG VCS_REF
ENV VCS_REF=$VCS_REF

ARG BUILD_DEPS="\
      git \
      make"
ENV BUILD_DEPS=$BUILD_DEPS

# ***** 安装依赖 *****
RUN set -eux && \
   # 修改源地址
   sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
   # 更新源地址并更新系统软件
   apk update && apk upgrade && \
   # 安装依赖包
   apk add --no-cache --clean-protected $BUILD_DEPS && \
   rm -rf /var/cache/apk/* && \
   # 更新时区
   ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime && \
   # 更新时间
   echo ${TZ} > /etc/timezone

# 运行工作目录
WORKDIR /build
# 克隆源码运行安装
RUN git clone --depth=1 -b ${TAGS} --progress https://github.com/Sansui233/proxypool.git /src && \
    cd /src && go mod download && make docker
# ##############################################################################


##########################################
#         构建基础镜像                    #
##########################################
#
# 指定创建的基础镜像
FROM alpine:latest

# 作者描述信息
MAINTAINER satrorn
# 时区设置
ARG TZ=Asia/Shanghai
ENV TZ=$TZ
# 语言设置
ARG LANG=C.UTF-8
ENV LANG=$LANG

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

# 工作目录
WORKDIR /proxypool-src

# 拷贝proxypool
COPY --from=0 /src/bin/proxypool-docker /proxypool-src/proxypool
COPY --from=0 /src/assets /proxypool-src/assets

# 授予文件权限
RUN set -eux && \
    mkdir -p /proxypool-src/conf/proxypool && \
    chmod +x /proxypool-src/proxypool && \
    chmod -R 775 /proxypool-src

# 增加配置文件
COPY ./conf/proxypool/config.yaml /proxypool-src/conf/proxypool/config.yaml
COPY ./conf/proxypool/source.yaml /proxypool-src/conf/proxypool/source.yaml

# 容器信号处理
STOPSIGNAL SIGQUIT

# 运行proxypool
CMD ["/proxypool-src/proxypool", "-c", "/proxypool-src/conf/proxypool/config.yaml", "-d"]
