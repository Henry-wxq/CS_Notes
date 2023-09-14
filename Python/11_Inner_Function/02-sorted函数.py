# 可以从任意序列的函数返回一个排好序的列表（列表！！！）

# 对字符串使用：
# 把每一个拆包以后按符号>数字>字母>中文
a = "111您,have a nive day!"
print(sorted(a))

# 对列表使用
# 按照首字母排序
b = ["ab","abb","a","bcc","b","x"]
print(sorted(b))

# 对字典使用
# 按照key排序
c = {1: "xhlisduhf", 3:"aasjdkbfkhjla"}
print(sorted(c))

# 对元祖使用
# 对其中每一个元素进行排序符号>数字>字母>中文
d = ("a","s","d","f","g","h")
print(sorted(d))


