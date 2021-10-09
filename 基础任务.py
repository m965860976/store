fahr = input("请输入华氏摄氏度")
fahr = float(fahr)
cent = (fahr - 32) / 1.8
print(cent)

r = input("请输入圆的半径")
r = float(r)
l = 2 * 3.14 * r
s = 3.14 * r * r
print(l)
print(s)

year = input("请输入年份")
year = int(year)
if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    print("该年是闰年")
else:
    print("该年不是闰年")

length = float(input("请输入长度"))
unit = input("请输入单位")
if unit == "英寸":
    print(length * 2.54)
elif unit == "厘米":
    print(length / 2.54)
else:
    print("别闹，这是英寸厘米转换的")

score = float(input("请输入成绩"))
if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("E")


a = float(input("请输入第一条边长"))
b = float(input("请输入第二条边长"))
c = float(input("请输入第三条边长"))
if a + b > c and a + c > b and b + c > a:
    print("能构成三角形")
    print("它的周长为：", a + b + c)
    side = (a + b + c) * (a + b - c) * (a + c - b) * (b + c - a)
    print("它的面积为：", 1 / 4 * pow(side, 0.5))
else:
    print("无法构成三角形")
