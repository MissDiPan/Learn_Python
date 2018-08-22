j = 0
for i in range(1, 101):
    j += i
print(j)


print(2)
for i in range(3, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    if j == (i-1):
        print(i)



