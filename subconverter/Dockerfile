# 指定构建的基础镜像
FROM tindy2013/subconverter

# 作者描述信息
LABEL maintainer="Satrorn <satrorn@gmaill.com>"

# 版本号
ENV VERSION 0.7.2

# 工作目录
WORKDIR /base

# 更新时间
RUN apk add tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

# 拷贝配置文件
COPY conf/ /base/config
COPY pref.yml /base
COPY groups.txt rulesets.txt /base/snippets/
COPY all_base.tpl Parents.yml /base/base/
COPY Country.list Line.list /base/rules/ACL4SSR/Clash/

EXPOSE 25500

WORKDIR /base

# 启动命令
CMD subconverter
