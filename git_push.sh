#!/bin/sh
#脚本功能：从提交最新代码到git
ssh -T git@github.com
remark=$(date +"%Y-%m-%d %H:%M:%S")
git remote -v
git add .
git pull origin
git commit -m "提交代码：${remark}"
git push -u origin master
git reset --hard origin/master
echo "---END---"