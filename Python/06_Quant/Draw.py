import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 提取的数据信息
data = {
    "年份": [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "市场规模（亿元）": [68909, 85486, 92195, 126911, 142759, 149277, 171760]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 设置图形样式
sns.set(style="whitegrid")

# 绘图
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x="年份", y="市场规模（亿元）", data=df, palette="Blues_d")
for index, row in df.iterrows():
    plt.text(index, row["市场规模（亿元）"] + 2000, f"{row['市场规模（亿元）']}", ha='center', va='bottom', fontsize=10)

plt.title("2017-2023年中国电子元器件市场规模", fontsize=14)
plt.ylabel("市场规模（亿元）", fontsize=12)
plt.xlabel("年份", fontsize=12)
plt.tight_layout()

# import ace_tools as tools; tools.display_dataframe_to_user(name="中国电子元器件市场规模数据", dataframe=df)
›
plt.show()
