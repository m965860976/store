# names = [
#     ["曹操", "56", "男", "106", "IBM", 500, "50"],
#     ["大乔", "19", "女", "230", "微软", 501, "60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700, "10"]
#         ]
# i = 0
# num = 0
# while i < len(names):
#     num = num + int(names[i][5])
#     i += 1
# print("平均薪资为", num/len(names))
# # 1.统计每个人的平均薪资
# i = 0
# age = 0
# while i < len(names):
#     age = age + int(names[i][1])
#     i += 1
# print("平均年龄为", age/len(names))
# # 2.统计每个人的平均年龄
# names.append(["刘备", "45", "男", "220", "alibaba", 500, "30"])
# print(names)
# # 3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
# i = 0
# pel = 0
# man = 0
# while i < len(names):
#     if names[i][2] == "女":
#         pel += 1
#         i += 1
#     elif names[i][2] == "男":
#         man += 1
#         i += 1
# print("公司男员工人数为", man)
# print("公司女员工人数为", pel)
# # 4.统计公司男女人数
#
#
#
# mt = [
#     ["罗恩", 23, 35, 44],
#     ["哈利", 60, 77, 68, 88, 90],
#     ["赫敏", 97, 99, 89, 91, 95, 90],
#     ["马尔福", 100, 85, 90]
#         ]
# i, j, goo = 0, 1, 0
# while i < len(mt):
#     j = 1
#     goo = 0
#     while j < len(mt[i]):
#         goo = goo + mt[i][j]
#         j += 1
#     print(mt[i][0], "的成绩为", goo)
#     i += 1


# num=int(input("请输入一个数"))
# while num != 0:
#     print(num%10)
#     num=num//10
# 输出1 2 3 4 5

a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
for i in range(1, len(a) - 1):
    for j in range(1, len(a) - i):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
print(a)
