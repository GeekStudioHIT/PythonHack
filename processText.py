# coding: utf-8

# 需求：在文本中所有的逗号后面加 "\n"

# 用于写入的文件
writeTo = open("./货架.txt", "w")

# 读取并处理文件
with open("./bucket_data.txt") as text:
    content = text.read()
    s = ''
    for c in content:
        if c == ',':
            c += '\n'
        s += c

    writeTo.write(s)
    writeTo.close()
