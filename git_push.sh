#!/bin/sh
#脚本功能：从提交最新代码到git
ssh -T git@github.com
remark=$(date +"%Y-%m-%d %H:%M:%S")
echo ".登陆状态"
git remote -v
git add .
git pull origin
echo ".文件下载完成"
git commit -m "提交代码：${remark}"
git push -u origin master
git reset --hard origin/master
echo ".文件更新完成"