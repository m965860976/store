# dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
# for i in dict:
#     print(i)           #1、请循环遍历出所有的key
#     print(dict[i])     #2、请循环遍历出所有的value
# dict["k4"] = "v4"      # 3、请在字典中增加一个键值对,"k4":"v4"
# print(dict)

# info = {
#     '苹果':32.8,
#     '香蕉': 22,
#     '葡萄': 15.5
# }
# dict1=(info)
# print(dict1["苹果"])

# fruits = {
#     "苹果": 12.3,
#     "草莓": 4.5,
#     "香蕉": 6.3,
#     "葡萄": 5.8,
#     "橘子": 6.4,
#     "樱桃": 15.8
# }
#
# fruits_m = {"小明": {"fruits": {"苹果": 4, "草莓": 13, "香蕉": 10}}}
# fruits_g = {"小刚": {"fruits": {"葡萄": 19, "橘子": 12, "樱桃": 30}}}
# m, g = 0, 0
# for i in fruits.keys():
#     if i in fruits_m["小明"]["fruits"]:
#         m=m+fruits[i]*fruits_m["小明"]["fruits"][i]
#     if i in fruits_g["小刚"]["fruits"]:
#         g=g+fruits[i]*fruits_g["小刚"]["fruits"][i]
#
# info = {
#     '小明': {
#         'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
#         'money': m
#     },
#     '小刚': {
#         'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
#         'money': g
#     }
# }
# print(info)

# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
# def count(list):
#     for i in list:
#         if i in dict3:
#             dict3[i] += 1
#         else:
#             dict3[i] = 1
#
# list = [21, 21, 21, 56, 56, 56, 56, 56, 56, 56, 56, 56, 10, 10, 10]
# dict3 = {}
# count(list)
# print(dict3)

names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]
dict4 = {}
for i in range(len(names)):
    dict4[names[i][0]] = names[i]
print(dict4)
