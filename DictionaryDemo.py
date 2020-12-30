"""
类似于map,在python中区别于list 是无序的
"""
dict = {}
dict['one'] = "1 + hello xiaowang"
dict[2] = "2+hello xiaowang"
tinydict = {'name': 'xiaowang', 'code': 1, 'site': 'www.baidu.com'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict['name'])
print(tinydict.keys())
print(tinydict.values())
