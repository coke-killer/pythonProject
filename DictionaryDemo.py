"""
类似于map,在python中区别于list 是无序的
"""
dict = {}
dict['one'] = "1 + hello xiaowang"
dict[2] = "2+hello xiaowang"
tinydict = {'name': 'xiaowang', 'code': 1, 'site': 'www.baidu.com'}
del tinydict['code']  # 删除键
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict['name'])
print(tinydict.keys())
print(tinydict.values())
tinydict.clear()
print(tinydict)  # 清空字典
del tinydict  # 删除字典
print(tinydict)
