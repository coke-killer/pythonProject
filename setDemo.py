"""
添加set demo,主要用来去重，创建一个空寂必须用set(),因为set{}是用来创建一个空字典
"""
sites = {'aaa', 'bbb', 'aaa', 'ccc', 'aaa'}
print(sites)
# 成员测试
if 'aaa' in sites:
    print('aaa 在集合中')
else:
    print('aaa 不在集合中')
# set  进行集合运算
a = set('abcdefghigklmn')
b = set('alacazm')
print(a)
print(a - b)  # a和b差集
print(a | b)  # 并集
print(a & b)  # 交集
print(a ^ b)  # 不同时存在的元素（并集与交集的差集）
