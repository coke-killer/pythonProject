# python的特色是用缩进表示代码块，不需要使用大括号{}
# 缩进空格数可变， 但是同一个代码块的语句必须包含相同空格数
if True:
    print("True")
else:
    print("False")
# 使用反斜杠表示一条语句，通常一行写完一条语句
total = item_one + \
        item_two + \
        item_three
# 在[]{}()中的语句不需要使用反斜杠\
total = ['item_one', 'item_two', 'item_three']
# 数字类型4种
"""
int
bool
float
complex 复数 1+2j
"""
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
