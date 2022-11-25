FROM node:lts-alpine AS dependencies

LABEL maintainer="Satrorn <satrorn@gmail.com>"
ENV VERSION 0.1.7

# ***** 安装依赖 *****
RUN apk add --no-cache bash git curl wget bash zip

# 克隆源码运行安装
RUN git clone --progress https://github.com/CareyWang/sub-web app
RUN curl -o /app/config.yaml 'https://api.loii.ml/sub?target=clash&url=https%3A%2F%2Fxn--4gq62f52gdss.com%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Dv61eheqezdgs3uvhztpmq4d7u65s40e1&insert=false&config=config%2FPart.ini'
