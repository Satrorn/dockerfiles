#############################
#     设置公共的变量         #
#############################
FROM alpine:latest as base

ENV VERSION 0.7.2

# 作者描述信息
MAINTAINER Satrorn
# 时区设置
ARG TZ=Asia/Shanghai
ENV TZ=$TZ
# 语言设置
ARG LANG=C.UTF-8
ENV LANG=$LANG

# 镜像变量
ARG DOCKER_IMAGE=satrorn/subconverter
ENV DOCKER_IMAGE=$DOCKER_IMAGE
ARG DOCKER_IMAGE_OS=subconverter
ENV DOCKER_IMAGE_OS=$DOCKER_IMAGE_OS
ARG DOCKER_IMAGE_TAG=latest
ENV DOCKER_IMAGE_TAG=$DOCKER_IMAGE_TAG

# ##############################################################################

####################################
#       构建subconverter            #
####################################
FROM base AS builder

# 作者描述信息
MAINTAINER danxiaonuo
# 时区设置
ARG TZ=Asia/Shanghai
ENV TZ=$TZ
# 语言设置
ARG LANG=C.UTF-8
ENV LANG=$LANG

# 构建安装依赖
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
   
# ##############################################################################

# 工作目录
WORKDIR /base
	
# 安装subconverter
RUN set -eux \
    && wget --no-check-certificate -P /base https://github.com/tindy2013/subconverter/releases/latest/download/subconverter_linux64.tar.gz -O /base/subconverter_linux64.tar.gz \
    && tar xzf subconverter_linux64.tar.gz \
    && rm -rf subconverter_linux64.tar.gz

# 复制配置文件
RUN cp -rf conf/base/all_base.tpl /base/subconverter/base
RUN cp -rf conf/base/Parents.yml /base/subconverter/base
RUN cp -rf conf/rules /base/subconverter/rules
RUN cp -rf conf/config /base/subconverter/config

# 容器信号处理
STOPSIGNAL SIGQUIT

# 启动命令
CMD ["./subconverter/subconverter"]
