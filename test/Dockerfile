# 指定构建的基础镜像
FROM alpine:latest AS builder

# ***** 安装依赖 *****
RUN apk add --no-cache bash git curl wget bash zip

# 克隆源码运行安装
RUN git clone --progress https://github.com/CareyWang/sub-web app

# 指定创建的基础镜像
FROM alpine:latest
COPY --from=builder /app /app
RUN cd /app && npm install && npm run build
