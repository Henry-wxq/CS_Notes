# 迭代数列时想跟踪当前序号
# enumerate函数可以返回一个元祖：(i, value)
word_list = ["foolish", "stupid", "idiot"]

# 建立一个空字典，使返回值可以调用字典方法
store = {}

# enumerate 语句使用如下：
for i, v in enumerate(word_list):
    # 向字典中添加元素的方法，前面的是key
    store[i] = v

# 取出对应的key即可
print(store[0])

print(store)