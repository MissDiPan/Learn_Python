f = open('test.txt')
lines = f.readlines()
count = {}
for line in lines:
    tokens = line.strip().split(' ')  # strip 去掉首位空格空行影响
    for token in tokens:
        if token not in count:
            count[token] = 0
        count[token] += 1

for word in count:
    print(word, count[word])