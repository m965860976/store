dict = {}
li = []
f = open(file='baidu_x_system.log', mode='r+', encoding='utf-8')

line = f.readline()
while line:
    a = line.split()
    b = a[0:1]  # 选取需要读取的位数
    li.append(b)  # 添加到列表中
    line = f.readline()
f.close()

for i in li:
    for j in i:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
print(dict)
