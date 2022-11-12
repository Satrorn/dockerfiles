#############################
#     设置公共的变量         #
#############################
FROM --platform=$BUILDPLATFORM alpine:latest AS base
# 作者描述信息
MAINTAINER satrorn
# 时区设置
ARG TZ=Asia/Shanghai
ENV TZ=$TZ
# 语言设置
ARG LANG=C.UTF-8
ENV LANG=$LANG

# 镜像变量
ARG DOCKER_IMAGE=satrorn/nginx
ENV DOCKER_IMAGE=$DOCKER_IMAGE
ARG DOCKER_IMAGE_OS=alpine
ENV DOCKER_IMAGE_OS=$DOCKER_IMAGE_OS
ARG DOCKER_IMAGE_TAG=latest
ENV DOCKER_IMAGE_TAG=$DOCKER_IMAGE_TAG

# ##############################################################################

# ***** 设置变量 *****

# 工作目录
ARG NGINX_DIR=/data/nginx
ENV NGINX_DIR=$NGINX_DIR
# NGINX环境变量
ARG PATH=/data/nginx/sbin:$PATH
ENV PATH=$PATH
# 源文件下载路径
ARG DOWNLOAD_SRC=/tmp/src
ENV DOWNLOAD_SRC=$DOWNLOAD_SRC

# luajit2
# https://github.com/openresty/luajit2
ARG LUAJIT_VERSION=2.1-20220411
ENV LUAJIT_VERSION=$LUAJIT_VERSION
ARG LUAJIT_LIB=/usr/local/lib
ENV LUAJIT_LIB=$LUAJIT_LIB
ARG LUAJIT_INC=/usr/local/include/luajit-2.1
ENV LUAJIT_INC=$LUAJIT_INC
ARG LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH

# ngx_devel_kit
# https://github.com/simpl/ngx_devel_kit
ARG NGX_DEVEL_KIT_VERSION=0.3.1
ENV NGX_DEVEL_KIT_VERSION=$NGX_DEVEL_KIT_VERSION

# lua-nginx-module
# https://github.com/openresty/lua-nginx-module
ARG LUA_NGINX_MODULE_VERSION=0.10.21
ENV LUA_NGINX_MODULE_VERSION=$LUA_NGINX_MODULE_VERSION

# nginx-sticky-module-ng
# https://github.com/Refinitiv/nginx-sticky-module-ng
ARG NGINX_STICKY_MODULE_NG_VERSION=1.2.6
ENV NGINX_STICKY_MODULE_NG_VERSION=$NGINX_STICKY_MODULE_NG_VERSION

# nginx-http-concat
# https://github.com/alibaba/nginx-http-concat
ARG NGINX_HTTP_CONCAT_VERSION=1.2.2
ENV NGINX_HTTP_CONCAT_VERSION=$NGINX_HTTP_CONCAT_VERSION

# ngx_lua_waf
# https://github.com/loveshell/ngx_lua_waf
ARG NGX_LUA_WAF_VERSION=0.7.2
ENV NGX_LUA_WAF_VERSION=$NGX_LUA_WAF_VERSION

# lua-resty-core
# https://github.com/openresty/lua-resty-core
ARG LUA_RESTY_CORE_VERSION=0.1.23
ENV LUA_RESTY_CORE_VERSION=$LUA_RESTY_CORE_VERSION
ARG LUA_LIB_DIR=/usr/local/share/lua/5.1
ENV LUA_LIB_DIR=$LUA_LIB_DIR

# lua-resty-lrucache
# https://github.com/openresty/lua-resty-lrucache
ARG LUA_RESTY_LRUCACHE_VERSION=0.13
ENV LUA_RESTY_LRUCACHE_VERSION=$LUA_RESTY_LRUCACHE_VERSION

# headers-more-nginx-module
# https://github.com/openresty/headers-more-nginx-module
ARG OPENRESTY_HEADERS_VERSION=0.33
ENV OPENRESTY_HEADERS_VERSION=$OPENRESTY_HEADERS_VERSION

# lua-resty-cookie
# https://github.com/cloudflare/lua-resty-cookie
ARG CLOUDFLARE_COOKIE_VERSION=0.1.0
ENV CLOUDFLARE_COOKIE_VERSION=$CLOUDFLARE_COOKIE_VERSION

# lua-resty-dns
# https://github.com/openresty/lua-resty-dns
ARG OPENRESTY_DNS_VERSION=0.22
ENV OPENRESTY_DNS_VERSION=$OPENRESTY_DNS_VERSION

# lua-resty-memcached
# https://github.com/openresty/lua-resty-memcached
ARG OPENRESTY_MEMCACHED_VERSION=0.17
ENV OPENRESTY_MEMCACHED_VERSION=$OPENRESTY_MEMCACHED_VERSION

# lua-resty-mysql
# https://github.com/openresty/lua-resty-mysql
ARG OPENRESTY_MYSQL_VERSION=0.25
ENV OPENRESTY_MYSQL_VERSION=$OPENRESTY_MYSQL_VERSION

# lua-resty-redis
# https://github.com/openresty/lua-resty-redis
ARG OPENRESTY_REDIS_VERSION=0.30
ENV OPENRESTY_REDIS_VERSION=$OPENRESTY_REDIS_VERSION

# lua-resty-shell
# https://github.com/openresty/lua-resty-shell
ARG OPENRESTY_SHELL_VERSION=0.03
ENV OPENRESTY_SHELL_VERSION=$OPENRESTY_SHELL_VERSION

# lua-resty-upstream-healthcheck
# https://github.com/openresty/lua-resty-upstream-healthcheck
ARG OPENRESTY_HEALTHCHECK_VERSION=0.06
ENV OPENRESTY_HEALTHCHECK_VERSION=$OPENRESTY_HEALTHCHECK_VERSION

# lua-resty-websocket
# https://github.com/openresty/lua-resty-websocket
ARG OPENRESTY_WEBSOCKET_VERSION=0.09
ENV OPENRESTY_WEBSOCKET_VERSION=$OPENRESTY_WEBSOCKET_VERSION

# lua-upstream-nginx-module
# https://github.com/openresty/lua-upstream-nginx-module
ARG LUA_UPSTREAM_VERSION=0.07
ENV LUA_UPSTREAM_VERSION=$LUA_UPSTREAM_VERSION

# nginx-lua-prometheus
# https://github.com/knyar/nginx-lua-prometheus
ARG PROMETHEUS_VERSION=0.20220527
ENV PROMETHEUS_VERSION=$PROMETHEUS_VERSION

# stream-lua-nginx-module
# https://github.com/openresty/stream-lua-nginx-module
ARG OPENRESTY_STREAMLUA_VERSION=0.0.11
ENV OPENRESTY_STREAMLUA_VERSION=$OPENRESTY_STREAMLUA_VERSION

# NGINX
# https://github.com/nginx/nginx
ARG NGINX_VERSION=1.22.0
ENV NGINX_VERSION=$NGINX_VERSION
ARG NGINX_BUILD_CONFIG="\
    --prefix=${NGINX_DIR} \
    --sbin-path=${NGINX_DIR}/sbin/nginx \
    --modules-path=${NGINX_DIR}/modules \
    --conf-path=${NGINX_DIR}/conf/nginx.conf \
    --error-log-path=${NGINX_DIR}/logs/error.log \
    --http-log-path=${NGINX_DIR}/logs/access.log \
    --pid-path=${NGINX_DIR}/logs/nginx.pid \
    --lock-path=${NGINX_DIR}/logs/nginx.lock \
    --http-client-body-temp-path=${NGINX_DIR}/temp/client_temp \
    --http-proxy-temp-path=${NGINX_DIR}/temp/proxy_temp \
    --http-fastcgi-temp-path=${NGINX_DIR}/temp/fastcgi_temp \
    --http-uwsgi-temp-path=${NGINX_DIR}/temp/uwsgi_temp \
    --http-scgi-temp-path=${NGINX_DIR}/temp/scgi_temp \
    --add-module=${DOWNLOAD_SRC}/ngx_devel_kit-${NGX_DEVEL_KIT_VERSION} \
    --add-module=${DOWNLOAD_SRC}/lua-nginx-module-${LUA_NGINX_MODULE_VERSION} \
    --add-module=${DOWNLOAD_SRC}/nginx-http-concat-${NGINX_HTTP_CONCAT_VERSION} \
    --add-module=${DOWNLOAD_SRC}/lua-upstream-nginx-module-${LUA_UPSTREAM_VERSION} \
    --user=nginx \
    --group=nginx \
    --with-stream \
    --with-stream=dynamic \
    --with-stream_ssl_module \
    --with-stream_ssl_preread_module \
    --with-stream_realip_module \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_addition_module \
    --with-http_sub_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_mp4_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_stub_status_module \
    --with-http_auth_request_module \
    --with-threads \
    --with-stream \
    --with-stream_ssl_module \
    --with-http_slice_module \
    --with-mail \
    --with-mail_ssl_module \
    --with-file-aio \
    --with-http_v2_module \
    --with-http_image_filter_module \
    --with-ipv6 \
"
ENV NGINX_BUILD_CONFIG=$NGINX_BUILD_CONFIG

# 构建安装依赖
ARG BUILD_DEPS="\
      curl \
      g++ \
      geoip-dev \
      gzip \
      make \
      openssl-dev \
      pcre-dev \
      tar \
      zlib-dev"
ENV BUILD_DEPS=$BUILD_DEPS

ARG NGINX_BUILD_DEPS="\
    # NGINX
    alpine-sdk \
    bash \
    findutils \
    gcc \
    gd-dev \
    geoip-dev \
    libc-dev \
    libedit-dev \
    libxslt-dev \
    linux-headers \
    make \
    mercurial \
    openssl-dev \
    pcre-dev \
    perl-dev \
    zlib-dev"
ENV NGINX_BUILD_DEPS=$NGINX_BUILD_DEPS

####################################
#    构建支持LUA的Nginx             #
####################################
FROM base AS builder

# ***** 安装依赖 *****
RUN set -eux && \
   # 修改源地址
   sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
   # 更新源地址并更新系统软件
   apk update && apk upgrade && \
   # 安装依赖包
   apk add --no-cache --clean-protected $BUILD_DEPS $NGINX_BUILD_DEPS && \
   apk add --no-cache --virtual build-dependencies $BUILD_DEPS && \
   rm -rf /var/cache/apk/* && \
   # 更新时区
   ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime && \
   # 更新时间
   echo ${TZ} > /etc/timezone

# ##############################################################################
# ***** 创建相关目录 *****
RUN set -eux && \
    mkdir -pv ${DOWNLOAD_SRC} && \
    mkdir -p ${NGINX_DIR}/temp/client_temp && \
    mkdir -p ${NGINX_DIR}/temp/proxy_cache && \
    mkdir -p ${NGINX_DIR}/temp/proxy_temp && \
    mkdir -p ${NGINX_DIR}/temp/fastcgi_temp && \
    mkdir -p ${NGINX_DIR}/temp/uwsgi_temp && \
    mkdir -p ${NGINX_DIR}/temp/scgi_temp && \
    mkdir -p ${NGINX_DIR}/logs/hack

# ##############################################################################
# ***** 下载源码包 *****
RUN set -eux && \
    wget --no-check-certificate http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/nginx.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/luajit2/archive/v${LUAJIT_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/luajit2.tar.gz && \
    wget --no-check-certificate https://github.com/simpl/ngx_devel_kit/archive/v${NGX_DEVEL_KIT_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/ngx_devel_kit.tar.gz && \
    wget --no-check-certificate https://github.com/Refinitiv/nginx-sticky-module-ng/archive/${NGINX_STICKY_MODULE_NG_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/nginx-sticky-module-ng.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-nginx-module/archive/v${LUA_NGINX_MODULE_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-nginx-module.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-core/archive/v${LUA_RESTY_CORE_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-core.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-lrucache/archive/v${LUA_RESTY_LRUCACHE_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/ngx_cache_purge.tar.gz && \
    wget --no-check-certificate https://github.com/alibaba/nginx-http-concat/archive/${NGINX_HTTP_CONCAT_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/nginx-http-concat.tar.gz && \
    wget --no-check-certificate https://github.com/loveshell/ngx_lua_waf/archive/v${NGX_LUA_WAF_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/ngx_lua_waf.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/headers-more-nginx-module/archive/v${OPENRESTY_HEADERS_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/headers-more-nginx-module.tar.gz && \
    wget --no-check-certificate https://github.com/cloudflare/lua-resty-cookie/archive/v${CLOUDFLARE_COOKIE_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-cookie.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-dns/archive/v${OPENRESTY_DNS_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-dns.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-memcached/archive/v${OPENRESTY_MEMCACHED_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-memcached.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-mysql/archive/v${OPENRESTY_MYSQL_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-mysql.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-redis/archive/v${OPENRESTY_REDIS_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-redis.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-shell/archive/v${OPENRESTY_SHELL_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-shell.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-upstream-healthcheck/archive/v${OPENRESTY_HEALTHCHECK_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-upstream-healthcheck.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-resty-websocket/archive/v${OPENRESTY_WEBSOCKET_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-resty-websocket.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/lua-upstream-nginx-module/archive/v${LUA_UPSTREAM_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/lua-upstream-nginx-module.tar.gz && \
    wget --no-check-certificate https://github.com/knyar/nginx-lua-prometheus/archive/${PROMETHEUS_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/nginx-lua-prometheus.tar.gz && \
    wget --no-check-certificate https://github.com/openresty/stream-lua-nginx-module/archive/v${OPENRESTY_STREAMLUA_VERSION}.tar.gz \
    -O ${DOWNLOAD_SRC}/stream-lua-nginx-module.tar.gz && \
    cd ${DOWNLOAD_SRC} && for tar in *.tar.gz;  do tar xvf $tar -C ${DOWNLOAD_SRC}/; done

# ##############################################################################
# ***** 安装中间件 *****
RUN set -eux && \
    # 安装LUAJIT
    cd ${DOWNLOAD_SRC}/luajit2-${LUAJIT_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装LUA_RESTY_CORE
    cd ${DOWNLOAD_SRC}/lua-resty-core-${LUA_RESTY_CORE_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装PROMETHEUS
    mv ${DOWNLOAD_SRC}/nginx-lua-prometheus-${PROMETHEUS_VERSION}/*.lua ${LUA_LIB_DIR}/ && \
    # 安装LUA_RESTY_LRUCACHE
    cd ${DOWNLOAD_SRC}/lua-resty-lrucache-${LUA_RESTY_LRUCACHE_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装CLOUDFLARE_COOKIE
    cd ${DOWNLOAD_SRC}/lua-resty-cookie-${CLOUDFLARE_COOKIE_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装OPENRESTY_DNS
    cd ${DOWNLOAD_SRC}/lua-resty-dns-${OPENRESTY_DNS_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装OPENRESTY_MEMCACHED
    cd ${DOWNLOAD_SRC}/lua-resty-memcached-${OPENRESTY_MEMCACHED_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装OPENRESTY_MYSQL
    cd ${DOWNLOAD_SRC}/lua-resty-mysql-${OPENRESTY_MYSQL_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装OPENRESTY_REDIS
    cd ${DOWNLOAD_SRC}/lua-resty-redis-${OPENRESTY_REDIS_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装OPENRESTY_SHELL
    cd ${DOWNLOAD_SRC}/lua-resty-shell-${OPENRESTY_SHELL_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装OPENRESTY_HEALTHCHECK
    cd ${DOWNLOAD_SRC}/lua-resty-upstream-healthcheck-${OPENRESTY_HEALTHCHECK_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install && \
    # 安装OPENRESTY_WEBSOCKET
    cd ${DOWNLOAD_SRC}/lua-resty-websocket-${OPENRESTY_WEBSOCKET_VERSION} && \
    make -j$(($(nproc)+1)) && make -j$(($(nproc)+1)) install

# ***** 安装NGINX *****
RUN set -eux && \
    cd ${DOWNLOAD_SRC}/nginx-${NGINX_VERSION} && \
    # sed -i '1,/nginx_version/{s/.*nginx_version.*/#define nginx_version      1010/}' src/core/nginx.h && \
    # sed -i '1,/NGINX_VERSION/{s/.*NGINX_VERSION.*/#define NGINX_VERSION      "1.1"/}' src/core/nginx.h && \
    sed -i '14s#nginx#xiaonuo_waf#' src/core/nginx.h && \
    sed -i '1,/NGINX_VAR/{s/.*NGINX_VAR.*/#define NGINX_VAR          "XIAONUO_WAF"/}' src/core/nginx.h && \
    sed -i 's#Server: nginx#Server: xiaonuo#g' src/http/ngx_http_header_filter_module.c && \
    sed -i 's#<hr><center>nginx</center>#<hr><center>xiaonuo</center>#g' src/http/ngx_http_special_response.c && \
    ./configure ${NGINX_BUILD_CONFIG} \
    --add-module=${DOWNLOAD_SRC}/headers-more-nginx-module-${OPENRESTY_HEADERS_VERSION} \
    --add-module=${DOWNLOAD_SRC}/stream-lua-nginx-module-${OPENRESTY_STREAMLUA_VERSION} \
    # --add-module=${DOWNLOAD_SRC}/nginx-sticky-module-ng-${NGINX_STICKY_MODULE_NG_VERSION} \
    --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' \
    --with-ld-opt='-Wl,-rpath,$LUAJIT_LIB -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie' \
    || ./configure ${NGINX_BUILD_CONFIG} \
    --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' \
    --with-ld-opt='-Wl,-rpath,$LUAJIT_LIB -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie' && \
    make -j$(($(nproc)+1)) build && \
    make -j$(($(nproc)+1)) install && \
    mv ${DOWNLOAD_SRC}/ngx_lua_waf-${NGX_LUA_WAF_VERSION} ${NGINX_DIR}/conf/waf

# ##############################################################################


##########################################
#         构建最新的镜像                  #
##########################################
FROM base
# 作者描述信息
MAINTAINER danxiaonuo
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
      ca-certificates \
      geoip-dev \
      openssl-dev \
      pcre-dev \
      zlib-dev"
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

# 拷贝文件
COPY --from=builder /usr/local/lib /usr/local/lib
COPY --from=builder /usr/local/share/lua /usr/local/share/lua
COPY --from=builder /data /data

# 拷贝配置文件
COPY conf/nginx/nginx.conf /data/nginx/conf/nginx.conf
COPY conf/nginx/gzip.conf /data/nginx/conf/gzip.conf
COPY conf/nginx/cache.conf /data/nginx/conf/cache.conf
COPY conf/nginx/proxy.conf /data/nginx/conf/proxy.conf
COPY conf/nginx/php.conf /data/nginx/conf/php.conf
COPY conf/nginx/websocket.conf /data/nginx/conf/websocket.conf
COPY conf/nginx/waf.conf /data/nginx/conf/waf.conf
COPY conf/nginx/waf /data/nginx/conf/waf
COPY conf/nginx/ssl /ssl
COPY conf/nginx/vhost /data/nginx/conf/vhost
COPY www /www

# 安装相关依赖
RUN set -eux && \
    apk add --no-cache --virtual .gettext gettext && \
    mv /usr/bin/envsubst /tmp/ && \
    runDeps="$( \
        scanelf --needed --nobanner ${NGINX_DIR}/sbin/nginx ${NGINX_DIR}/modules/*.so ${LUAJIT_LIB}/*.so /tmp/envsubst \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" && \
    apk add --no-cache --virtual .$NGINX_BUILD_DEPS $runDeps && \
    apk del .gettext && \
    mv /tmp/envsubst /usr/local/bin/


# 将请求和错误日志转发到docker日志收集器
RUN set -eux && \
    ln -sf /dev/stdout /data/nginx/logs/access.log && \
    ln -sf /dev/stderr /data/nginx/logs/error.log && \
# 创建用户和用户组
    addgroup -g 32548 -S nginx && \
    adduser -S -D -H -u 32548 -h /var/cache/nginx -s /sbin/nologin -G nginx -g nginx nginx && \
# smoke test
# ##############################################################################
    ln -sf ${NGINX_DIR}/sbin/* /usr/sbin/ && \
    nginx -V && \
    nginx -t

# 自动检测服务是否可用
HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost/ || exit 1

# ***** 监听端口 *****
EXPOSE 80 443

# ***** 工作目录 *****
WORKDIR /data/nginx

# ***** 容器信号处理 *****
STOPSIGNAL SIGQUIT

# ***** 启动命令 *****
CMD ["nginx", "-g", "daemon off;"]
