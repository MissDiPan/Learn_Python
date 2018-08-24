# 元组，可以视为不可变的列表，赋值后不可二次更改

tuple_a = ("str", 1, ["a", "b", "c"], 4)
tuple_b = ("hello",)
print(tuple_a[0])
print(tuple_a[1:3])
print(tuple_a[1:])
print(tuple_b * 2)
print(tuple_a + tuple_b)
