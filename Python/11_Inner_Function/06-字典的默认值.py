# get(key,value)返回字典里key的值，如果没有，会返回value(若没有设置，则自动默认为None)
# 如果没有value不会报错
# pop(key,value)返回字典里key的值，如果没有，会返回value
# 如果没有设置value会报错

dic1 = {1:"Jackie", 2:"Henry", 3:"Levi", 4:"Leon"}

x = dic1.get(5, "Bob")
y = dic1.get(5)
# z = dic1.pop(5)

print(x)
print(y)
print(dic1)

# 通过首字母，将列表中的单词分类
words = ["append", "abandon", "affect", "suggest", "support"]
word = {}
for word2 in words:
    first_letter = word2[0]
    if first_letter not in word:
        # 注意，这里word2一定要加中括号构成一个列表，不然无法在后面增加同一个首字母开头的单词
        word[first_letter] =[word2]
    else:
        word[first_letter].append(word2)

print(word)

# setdefault的应用
# setdefaout(keyname, value)
# keyname: 返回的键名
# value：若keyname已经存在，则无效；若不存在则成为此键的值
word3 = ["append", "abandon", "affect", "suggest", "support"]
word4 = {}
for word5 in word3:
    x = word4.setdefault(word5[0], []).append(word5)

print(word4)






