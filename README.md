# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Write your name on line 6, save it, and then head back to GitHub Desktop.

使用git的基本步骤

1、下载相关软件，如：git、GitHub Desktop
2、安装上述软件
3、在git上注册账号
3、做全局设置
	git config --global user.name "charles809"
	git config --global user.email "charles809@sina.com"
4、在本地生成SSH Keys，并将id_rsa.pub文件注册到github账户设置中
	ssh-keygen -t rsa -C "charles809@sina.com"
5、GitHub认证通信
	ssh -T git@github
6、在GitHub网页上创建仓库（使用GitHub desktop也可以）
7、连接仓库
8、clone已有仓库
9、在clone的本地仓库编写代码文件
10、使用git add命令将代码文件提交至暂存区
11、使用git push命令将代码文件加入到仓库

使用git的实际操作（完成基本步骤1-5之后）
0、在GitHub上建立远程仓库
1、建立本地文件夹
2、进入刚建立的文件夹
3、初始化本地仓库
4、确认本地仓库的分支名称
5、设置本地仓库的远程仓库：git remote add
	git remote add origin git@github.com:charles809/grepos.git
6、推送至远程仓库：git push
	git push -u origin master
7、获取远程仓库：git clone
	git clone git@github.com:charles809/grepos.git
8、查看当前分支信息：git branch -a
9、获取当前仓库的另一远程分支：git checkout -b feature-D origin/feature-D

网站给出的标准流程

…or create a new repository on the command line

echo "# gitNotability" >> README.md #把语句加入文件末尾
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/charles809/gitNotability.git
git push -u origin main


…or push an existing repository from the command line

git remote add origin https://github.com/charles809/gitNotability.git
git branch -M main
git push -u origin main

# gitNotability


