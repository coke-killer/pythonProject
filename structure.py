# 斐波那契数列
a, b = 0, 1
while b < 10:
    print(b, end=",")
    a, b = b, a + b
# if ,else
a = 1
if a == 2:
    print(a, end="")
elif a == 1:
    print(a, end="")
else:
    print(a, end="")
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print("1到%d之和为:%d" % (n, sum))
