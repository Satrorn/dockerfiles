#!/bin/sh
#脚本功能：从git拉取最新代码
pwddir=$(cd $(dirname $0); pwd)
echo $pwddir
cd $(dirname $0)
git fetch --all
git reset --hard origin/main