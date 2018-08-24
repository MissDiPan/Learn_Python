# set是无序集合
bri = set(['brazil','russia', 'india'])
print('india' in bri)

bric = bri.copy()
bric.add('China')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri & bric)
