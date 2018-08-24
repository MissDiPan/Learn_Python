f = open('test.txt', 'r')
while True:
    lines = f.readlines(1)  # 读取行
    if not lines:
        break
    for line in lines:
       print(line.strip())
f.close()