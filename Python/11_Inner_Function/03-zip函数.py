# 使用zip可以跨数据类型进行组合
# zip组合出来的是元祖
# zip可以处理任意多的序列，元素的个数取决于最短的序列
# 需要用list在输出前进行包裹
# 直接用print会出现：<zip object at 0x7fade7485940>


# 对列表使用zip：
a = ["a","b"]
b = ["c","d"]
test_1 = zip(a, b)
print(list(test_1))

# 对字典使用zip：
# 输出的是key的组合元祖
c = {1: "e", 2: "f", 3: "g"}
d = {4: "h", 5: "i", 6: "j"}
test_2 = zip(c, d)
print(list(test_2))

# 对字符串使用zip：
# zip可以处理任意多的序列，元素的个数取决于最短的序列
e = "afbaksjdfbjhsad"
f = "kyasgfahbfou"
test_3 = zip(e, f)
print(list(test_3))

# 对元祖使用zip：
g = (1,2,3,6,5,7,9)
h = ("a","b""g","v","l")
test_4 = zip(g,h)
print(list(test_4))

# 不同数据类型可以组合成同一个元祖
try:
    test_5 = zip(a, c)
    print(list(test_5))

except Exception:
    print("%s错误" % test_5)

# 同时迭代多个序列，结合enumerate
# 数据接收时要使用跟返回数据相同类型的接收（如果想要把里面的数据独立出来，如下面的x,y）
# format方法是字符串特有的方法，用{}作为占位符，把后面的数据填充进去
for i, (x, y) in enumerate(zip(a, b)):
    print("{}:{},{}".format(i,x,y))

# 如果不把数据单独定义到一个变量中，那么就不是那么好看
for i, z in enumerate(zip(a,b)):
    print("{}:{}".format(i, z))

# 给出一个“被压缩的”序列，zip可以被用来解压序列也可以当作把行的列表转换为列的列表
# 注意要在zip中的变量前加上*，不然会提示value太多
i = [(1,2),(3,4),(5,6)]
j, k = zip(*i)
print(j)
print(k)