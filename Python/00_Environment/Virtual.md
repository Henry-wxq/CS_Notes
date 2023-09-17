1. 使用venv在terminal中启动及配置
    1. cd到想要建设虚拟环境的directory
    2. （python -m venv -h 查看帮助）
    3. python -m venv [Name] 创建虚拟环境
    4. cd 进入Name
    5. cd 进入Scripts
    6. 输入activate激活，不用管后缀，激活成功前面就会带上后缀，不一定需要输入激活，只要到这个路径里面就可以直接使用
    7. 就可以使用pip安装到虚拟环境中了
    8. deactivate去激活

2. IDE中配置虚拟环境
    1. 选择到Name下Scripts中的python.exe即可
    2. PyCharm - File - New Project - Existing intepreter - ...... - [Name] - Scripts - python.exe
