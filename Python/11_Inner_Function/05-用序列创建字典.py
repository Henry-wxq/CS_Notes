# 创建空字典
empty_dict = {}

# 使用zip函数导入数据
bed_num = [1,2,3,4]
bed_name = ["Jackie","Henry","Levi","Leon"]

# 给空字典内导入变量
for a, b in zip(bed_num,bed_name):
    empty_dict[a] = b

print(empty_dict)
