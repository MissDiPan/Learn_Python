# 字典，类似c++的map， key-value键值对的集合，无序的容器
# 比遍历查找快很多

dict_a = {
    "name":"Alan",
    "age":24,
    1: "level_1"
}

print(dict_a["name"])
print(dict_a["age"])
print(dict_a[1])

print("name" in dict_a)  # 判断key是否在字符里
print("xxx" in dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

dict_a.get("like", "not exist")  # 如果存在key"like"，则返回值，不存在返回"not exist"
dict_a["like"] = "Apple"  # 增加一个list
dict_a.pop("like")  # 因为无序，所以必须指定删除哪组
dict_a.keys()