# ***** 安装依赖 *****
RUN apk add --no-cache bash git curl wget bash zip

# 克隆源码运行安装
RUN git clone --progress https://github.com/CareyWang/sub-web.git /sub-web
COPY conf/sub-web/.env /sub-web/.env
COPY conf/sub-web/Subconverter.vue /sub-web/src/views/Subconverter.vue