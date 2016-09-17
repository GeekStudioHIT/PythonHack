#coding:utf8
# 功能介绍 : 将文本文件中每一行的结尾都加上两个空格
# 应用场景 : 将简书中的MarkDown向Github中移植的时候总是会出现不换行的问题 , 此脚本主要用于解决该问题
# 作者 : 王一航
# 时间 : 2016/09/17
fileName = "README.md" # 文件名
file = open(fileName, "r")
lines = file.readlines() # 一次性将文件全部读进内存
number = len(lines); # 获取行数
for i in range(0, number):
	if lines[i].endswith("  \n"):
		continue
	elif lines[i].endswith(" \n"):
		lines[i] = lines[i][:-2] + "  \n"
	elif lines[i].endswith("\n"):
		lines[i] = lines[i][:-1] + "  \n"
	else:
		lines[i] += "  \n" # 处理文件结尾
file.close()

# 将文件内容的列表写入文件
file = open(fileName, "w+")
for i in range(0, number):
	file.write(lines[i])
file.close()
