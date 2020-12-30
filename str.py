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
# 输出最后一个字符
print(str[-1])
# 输出第一个至导数第二个字符
print(str[0:-1])
# 输出第一个字符
print(str[0])
# 输出第2个至第4个字符
print(str[2:5])
# 输出第三个开始后的所有字符
print(str[2:])
# 输出第二个到第五个且且间隔3个的字符
print(str[1:6:3])
# 连续输出字符串两次
print(str * 2)
# 连接字符串
print(str + '你好')
print('---------------')
# 转义输出
print('hello\n world')
# 非转义输出
print(r'hello\n world')

# 等待用户输入
# input("\n\n 按下enter后退出")
#同一行使用多条语句
import sys;x='hello world'; sys.stdout.write(x+'\n')
# print 默认输出不换行
print('--------')
str1='a'
str2='b'
#换行输出
print(str1)
print(str2)
print('--------')
#不换行输出
print( str1,end="")
print( str2,end="")
print('xxxxxxxx')