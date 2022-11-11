#!/bin/sh
#脚本功能：从提交最新代码到git
ssh -T git@github.com
remark=$(date +"%Y-%m-%d %H:%M:%S")
git remote -v
git add .
echo "---开始下载---合并网络版本---"
git pull origin
echo "---下载完成---开始提交更新版本---"
git commit -m "提交代码：${remark}"
git push -u origin master
git reset --hard origin/master
echo "---提交完成---结束---"