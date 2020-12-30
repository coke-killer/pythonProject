# 字符串
"""
单引号双引号一致
'\'转义字符
使用r可以不转义 r"this is a line with \n" 则\n会显示，并不是换行。
字面意义级联
如
“this" "is" "string" 会自动转换 this is string
用+拼接用*运算符重复
两种索引方式 左边0开始，右边-1开始
字符串不能改变，无字符类型，一个字符就是长度为1的字符串
字符串截取语法：变量[头下标：尾下标：步长]
"""
str = 'hello world'
print(str)
print(str[-1])
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:6:3])
print(str * 2)
print(str + '你好')
print('---------------')
print('hello\n world')
print(r'hello\n world')
