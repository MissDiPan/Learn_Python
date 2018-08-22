list_a = [1, 2, "test"]
for i in list_a:  # 遍历容器
    if i == 2:
        continue  # 直接开始循环的下一轮
    print(i)


for i in range(0, 10):  # 【0，10）
    for j in range(0, 10):
        # print(j)
        if j == 5:
            break  # 强制中止，只跳出j循环

