# Git Basic


## 对Git进行基本配置
1. 配置用户信息（名字及邮箱）
	```
	git config --global user.name '[Name]'
	git config --global user.email '[Email]'
	```
2. 为常用指令配置别名
打开用户目录，创建.bashrc文件，或者在git bash中执行touch ~/.bashrc
	```
	#用于输出git提交日志
	alias git-log='git log --pretty=oneline --all --graph --abbrev-commit'

	#用于输出当前目录所有文件及基本信息
	alias ll='ls -al'
	```

## Baisc Operation of Git

1. 克隆，即将远程仓库保存到本地
	```
	git clone [url]（建议使用SSH）
	# e.g. git clone https://github.com/Henry-wxq/Ticket_Snatching.git
	```

2. 版本回退(版本切换)
	```
	git reset --hard commitID
	# commitID可以使用git-log或者git log指令查看
	```

3. 查看已经删除的记录
	```
	git reflog
	```

4. 不让git管理文件: 有些时候我们不想把某些文件纳入版本控制中，比如数据库文件，临时文件，设计文件等；在主目录下建立"gitignore"文件，此文件有如下规则：

	1. 忽略文件中的空行或以井号（＃）开始的行将会被忽略。
	
	2. 可以使用Linux通配符。例如：星号（*）代表任意多个字符，问号（？）代表一个字符，方括号（[abc]）代表可选宇符范国，大括号（{string1,string2.…}）代表可选的字符串等。
	
	3. 如果名称的最前面有一个感叹号（！），表示例外规则，将不被忽略。
	
	4. 如果名称的最前面是一个路径分隔符（/），表示要忽略的文件在此目录下，而子目录中的文件不忽略。
	
	5. 如果名称的最后面是一个路径分隔符（/），表示要忽路的是此目录下该名称的子目录，而非文件（默认文件或目录都忽略）。

	```
	*. txt		# 忽略所有 •txt结尾的文件，这样的话上传就不会被选中！
	!lib.txt	# 但1ib.txt除外
	/temp		# 仅忽略项目根目录下的TODO文件，不包括其它目录temp
	build/		# 忽略bui1d/日录下的所有文件
	doc/*.txt	# 会忽略 doc/notes, txt_ 但不包括 doc/serverlarch. txt
	```

5. 分支：只能同时对一个分支进行修改，正常来说一个项目中每个人负责有一个分支，互不影响；HEAD指向的就是当前的分支
	```
	# 1. 查看分支
	git branch
	
	# 2. 创建分支
	git branch [分支名字]
	
	# 3. 切换分支
	git checkout [分支名字]
	
	# 4. 创建并切换分支
	git checkout -b [分支名字]
	
	# 5. 合并分支：
	git merge [分支名字]（被合并的分支）
	
	# 6. 删除分支
	git branch -d [分支名字]
	```
		
6. 解决冲突：两个分支改了同一个文件同一行的代码
	1. 处理文件冲突的地方（在merge的时候会自动出现两个版本）
	2. 将解决完冲突的文件加入暂存区（add）
	3. 提交到仓库（commit）（vim中esc+:wq为保存退出）

7. 分支的使用原则与流程 （D:\Files\Photos\）
	1. master分支(一般不会删除)：线上分支，主分支，中小规模项目作为线上运行的应用对应的分支
	2. develop分支（一般不会删除）：从master创建的分支，一般作为开发部门的主要开发分支，如果没有其它并行开发不同期上线要求，都可以在此版本进行开发，阶段开发完成后，需要时合并到master分支，准备上线
	3. feature/xxxxx分支：从develop创建的分支，一般是同期并行开发，但不同期上线时创建的分支，分支上的研发任务完成后，合并到develop分支
	4. hotfix/xxxxx分支：从master派生的分支，一般作为线上bug修复使用，修复完成后需要合并到master、test、develop分支
	5. 还有一些其它分支，例如test分支，pre分支（预上线分支

8. 强制删除分支：当分支代码没有完全merge到主分支时，需要使用D来进行删除
	```
	git branch -D [分支名字]
	```

9. 配置SSH公钥
	```
	# 1. 生成SSH公钥
	ssh-keygen -t rsa
	# 不断回车，若公钥已经存在则自动覆盖
	
	# 2. 获取公钥
	cat ~/.ssh/id_rsa.pub
	
	# 3. 验证是否配置成功
	ssh -T git@github.com

10. 操作远程仓库
	```
	# 1.添加远程仓库(先初始化本地仓库，然后与已创建的远程仓库进行对接)
	git remote add [远端名称] [仓库路径]
	# e.g. remote add origin git@github.com:Henry-wxq/Git_Study.git
	# 远端名称，默认时origin，取决于远端服务器配置
	
	# 2. 查看远程仓库
	git remote
	
	# 3. 推送到远程仓库
	git push [远端名称] [本地分支名]:[远端分支名]
	# e.g. git push origin master:master
	
	git push -f [远端名称] [本地分支名]:[远端分支名]
	# -f表示强制覆盖
	
	git push --set-upstream [远端名称] [本地分支名]:[远端分支名]
	# 推送到远端的同时，建立起和远端分支的关联关系，下次再推的时候可以直接使用git push（用git brach -vv查看是否关联成功）
		
	# 4. 第一次推送的完整代码：
	git push -f --set-upstream [远端名称] [本地分支名]:[远端分支名]
	
	# 5. 从远端仓库克隆： 即将远程仓库保存到本地
	git clone [url] [本地目录]
	# e.g. git clone https://github.com/Henry-wxq/Ticket_Snatching.git
	
	# 6. 从远程仓库抓取:抓到本地但不会合并
	git fetch [远端名称/分支名称]（若后面不写则抓取所有分支）
	git merge [远端branch]
	
	# 7. 从远程仓库拉取: fetch+merge
	git pull [远端名称/分支名称]

11. 在IDEA中使用git: 将idea中terminal改成git bash：Setting - Tool - Terminal - shell path改成Git/bin/bash.exe所在目录
		
	
	
	
