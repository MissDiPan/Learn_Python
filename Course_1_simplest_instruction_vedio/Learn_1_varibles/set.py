# 可以看作没有value的list，只存key，去重或求并求交

girls_1 = set(['Lucy', 'Lily'])
girls_2 = set(['Lily', 'Anna'])

girls_1 & girls_2  # 求交
girls_1 | girls_2  # 求并

girls_1.add('Marry')  # 如果和之前有重复，会自动去重
girls_1.remove('Lucy')
len(girls_1)