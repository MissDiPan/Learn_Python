# 查找
s = "abc"
s.find("b")  # 返回首个字符所在的下标
s.find("bc")
s.find("xx")  # -1是没查到

# 分割
s = "aa12bb12cc"
s.split('12')  # 以'12'为分割符，返回列表

# 大小写转换
s.upper()
s.lower()

# 截取
s = '12345'
s[2:5]
s[2:]
s[3:-1]  # 这个- 1 相当于 Matlab 里的 end-1
s[1:5:2]  # 从1到4 每隔两个

# 追加
s = 'abc'
t = 'def'
s + t

# 替换
s = '1,2,3'
s.replace(',', '#')

# 链接
s = ['a', 'b', 'c']
'#'.join(s)

# 反转
s[::2]  # 隔两个取
s[::-1]  # 字符串反向


