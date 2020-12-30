import sys

print('=====================python import mode')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import argv, path  # 导入特定成员

print('path:', path)
