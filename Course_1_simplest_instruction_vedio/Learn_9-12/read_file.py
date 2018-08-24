import sys
import os

# 获取当前文件夹的绝对路径
base_dir = os.getcwd()
# 拼接文件夹路径和test.txt文件路径
file_dir = os.path.join(base_dir,'data','test.txt')
# 写文件/打开文件
file = open('test.txt', 'w')  # w: write, r: read
file.write('Hello world!')
file.close()

f = open('test.txt')
content = f.read()  # 如果文件太大，容易崩
f.close()
print(content)

f = open('test.txt', 'w')
f.writelines(['hhhhhhhh', '233333333'])  # 写列表
f.close()

f = open('test.txt', 'w')
f.write('hhhhhhhh233333333')  # 写单个字符串
f.close()

f = open('test.txt', 'a')  # 追加编辑
f.writelines(['\nlalalalal', '\nlueluelue'])  # 分行
f.close()