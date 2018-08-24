class Human(object):
    pass

# 类属性
class Human(object):
    taisheng = True

# 实例属性
class Human(object):
    def __init__(self, name):    # 用这个语句定义某一个实例
        self.name = name  # 定义的name就是设置的第二个参量
    def walk(self):  # self 表示调用本身这个函数的参量
        print(self.name + " is walking")
    def get_name(self):
        return self.name
human_a = Human("alan")
human_a.walk()
print(human_a.name)
print(human_a.get_name())

# new example

class Human(object):
    def __init__(self, name):
        self.__name = name
    def get_name(self):  # get param
        return self.__name
    def set_name(self, name): # set param
        if len(name) <= 10:  # 只有小于10个字符才重命名
            self.__name = name
human_a = Human("alan")
# print(human_a.__name)  # 带下划线表示私有，只能get，不能直接调用
print(human_a.get_name())
human_a.set_name("bob")
print(human_a.get_name())


class Human(object):
    pass
human_a = Human()  # 声明一个实例
human_a.name = "alan"  # 定义name属性，属性可以在创建函数当时或之后任意时间设置
print(human_a.name)

# 继承，子类拥有父类的属性和方法，也可以拥有父类不具备的属性和方法
class Man(Human):  # 从Human这个类别继承
    def __init__(self, name, has_wife):
        self.__name = name  # 这里是一个特例，因为Humen只有一个属性name，否则特性设置全都要打一遍
        self.__has_wife = has_wife


class Man(Human):
    def __init__(self, name, has_wife):
        super(Man, self).__init__(name)  # 这里表示这些特性直接从父类继承
        self.__has_wife = has_wife
    def smoke(self):
        print("A man maybe smoke")
    def drink(self):
        print("A man maybe drink")


class Woman(Human):
    def __init__(self, name, has_husband):
        super(Woman, self).__init__(name)
        self.__has_husband = has_husband
    def shopping(self):
        print("A woman always go shopping")
    def make_up(self):
        print("A woman always make up")