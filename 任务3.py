import random
import math

# 输入十个数并求其和
sum = 0
for i in range(1, 11):
    n = int(input('请输入第{}个值：'.format(i)))
    sum += n
print(sum)

# 输入10个数并求其最大值、和、平均值
# list = []
# for i in range(1, 11):
#     list.append(int(input('请输入第{}个值：'.format(i))))
# print(max(list))
# print(sum(list))
# print(sum(list) / 10)

# 随机生成50~150的数
# ran = random.randint(50, 150)
# print(ran)

# 判断是否构成三角形
# a = int(input("请输入三角形的边长"))
# b = int(input("请输入三角形的边长"))
# c = int(input("请输入三角形的边长"))
# if a + b > c and a + c > b and b + c > a:
#     print("可以构成三角形")
#     if a == b or a == c or b == c:
#         print("构成的三角形为等腰三角形")
#     elif a == b == c:
#         print("构成的三角形为等边三角形")
#     elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
#         print("构成的三角形为直角三角形")
#     else:
#         print("构成的三角形为普通三角形")
# else:
#     print("无法构成三角形")

# 用+或-互换位置
# a = input("请输入数字A：")
# b = input("请输入数字B：")
# sign = input("请输入符号：")
# if sign == "+":
#     print("数字A：", b)
#     print("数字B：", a)
# elif sign == "-":
#     print("数字A：", a)
#     print("数字B：", b)

# 登录三次自动锁定
# tries = 1
# use = "root"
# code = "admin"
# while tries <= 3:
#     user = input("请输入用户名：")
#     password = input("请输入密码：")
#     if password == code:
#         print("登录成功")
#     else:
#         print("请重新输入 \n")
#         tries = tries + 1
# else:
#     print("欢迎下次再来")

# 杨辉三角形
# num = int(input('请输入行数：'))
# list1 = []
# for n in range(num):
#     row = [1]
#     list1.append(row)
#     if n == 0:
#         print(row)
#         continue
#     for m in range(1, n):
#         row.append(list1[n - 1][m - 1] + list1[n - 1][m])
#     row.append(1)
#     print(row)

# N×N的乘法表
# i = 1
# n = int(input("请输入："))
# while i <= n:
#     j = 1
#     while j <= i:
#         print(f'{i}*{j}={i * j}', end=" ")
#         j += 1
#     print()
#     i += 1

# 倒叙的九九乘法表
# for i in range(9, 0, -1):
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i * j}', end=" ")
#     print()

# 青蛙爬井
# high = 20
# frog = 0
# day = 1
# while True:
#     frog += 3
#     if frog >= high:
#         break
#     else:
#         day += 1
#         frog -= 2
# print(day)

# 左边的都合法，右边的都不合法

# 20以内的阶乘之和
# sum = 0
# for i in range(1, 21):
#     sum += math.factorial(i)
# print(sum)
