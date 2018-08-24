# 类似数组，一个有序可变集合的容器
# 支持内置基础数据结构甚至是列表，可支持嵌套
# 不同的数据结构可以放在同一个列表中，没有统一类型限制

list_a = ["str", 1, ["a", "b", "c"], 4]
list_b = ["hello"]
print(list_a[0])
print(list_a[1:3])
print(list_a[1:])
print(list_a[-1])  # the end one 4
print(list_b * 2)
print(list_a + list_b)

game = ["dota", "dota2", "lol"]
len(game)  # 这些在python console里输入
game[0]
game.append("wow")  # 追加元素(末尾增加)
game.insert(2, "wow")  # 制定位置插入，这里是第三个元素
game.pop()  # 删除最后一个元素
game.pop(0)
game[0] = "deleted"