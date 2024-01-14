# Vim

## Installation NeoVim (In Ubuntu)
1. sudo add-apt-repository ppa:neovim-ppa/stable
2. sudo apt-get install -y neovim

## 客制化NeoVim: 通过配置文件完成(vim: .vimrc)
1. 新建配置文件夹: mkdir ~/.config/nvim
2. 通过nvim新建配置文件进行更改键位等: nvim ~/.config/nvim/init.vim
3. 安装插件: 在VimAwesome上寻找合适插件，以The NERD tree为例子(文件浏览器插件)
	1. 强烈推荐使用VimPlug来安装插件
	2. 安装VimPlug：在google上搜索VimPlug，进入其github界面，复制对应系统的相应代码复制进行安装
	3. 需要在Ubuntu系统上先安装Curl: `sudo apt-get install curl`
	4. 回到配置文件: `nvim ~/.config/nvim/init.vim`
	5. 复制Github VimPlug markdown上Example对应的Example中开头和末尾的两行: `call plug#begin('~/.vim/plugged')`; `call plug#end()`
	6. 在这两行中间复制粘贴需要安装的插件的代码，从VimAwesome上进行复制: `Plug 'scrooloose/nerdtree'`
	7. 退出配置文件，再重新进入，进入命令模式: `PlugInstall` (可以使用`Tab`自动补全)
	8. 使用`:q`退出安装完成的界面
	9. 进入命令模式，输入`NERDTree`回车便可看到文件浏览器
	10. 使用o可以打开文件夹




## 普通模式
1. 光标向左：`h`; 下：`j`; 上：`k`; 右：`l`
2. 向下跳转4行：`4j` (同理hkl)
3. 跳转到下个单词的开头: `w`
4. 跳转到前一个单词的开头: `b`
5. 跳转到文件最前方：`gg`
6. 跳转到文件最下方: `G`
7. 向上翻页: `Ctrl + d`; 向下翻页: `Ctrl + d`
8. 移动到离光标最近的字母: `f + (字母)`
9. 复制: `y`; 粘贴: `u`
10. 复制当前单词: `yaw` (yank all words)
11. 复制包括当前行的向下4行: `y4k` (y后可以加入多种指令, e.g., 4k, 8l)
12. 删除当前行: `dd`; 删除当前单词: `dw`; 删除到最近的r为止的内容: `dfr`; 删除左边字母: `dh`(jkl同理)
13. 撤销: `u`
14. 在光标前面插入空行：`O`；后面：`o`
15. 回到行末: `A`; 回到行首: `I`
16. 增加缩进: `>>`; 减少缩进: `<<`
17. 改变(类似删除但是会增加一个并进入编辑模式的功能)整个单词: `caw` (change all word) (直接删除当前单词并进入输入模式)
18. 删除这一行并进入输入模式: `cc`

## 编辑模式
1. 光标前开始输入: `i`; 光标后开始输入: `a` (append)
2. 从当前行开始进行输入: `I`; 行末: `A`
2. 退出输入模式: `Esc`

## 命令模式: 在普通模式下输入`:` 进入命令模式，使用`Esc`退出
1. 退出文件: `q`
2. 保存文件: `w`
3. 保存并退出: `wq`

## 可视模式: 在普通模式下输`v`, 再次输`v`退出，用来选中内容
1. 移动光标即可选中内容
2. 复制内容: `y`
3. 删除内容: `d`
4. 删除内容并进入编辑模式: `c`

