class pphone:
    __name = ""
    __sex = ""
    __age = 0
    __cost = 0
    __sign = ""
    __battery = 0  # 电池容量
    __size = 0
    __dtime = 0  # 待机时长
    __integral = 0  # 积分

    def setname(self, name):
        if name == "":
            print("不能为空")
        else:
            self.__name = name

    def getname(self):
        return self.__name

    def setsex(self, sex):
        if sex != "男" or sex != "女":
            print("你是个啥玩意？")
        else:
            self.__sex = sex

    def getsex(self):
        return self.__sex

    def setage(self, age):
        if age < 0 or age > 120:
            print("你真nb")
        else:
            self.__age = age

    def getage(self):
        return self.__age

    def setcost(self, cost):
        if cost < 0:
            print("欠费了")
        else:
            self.__cost = cost

    def getcost(self):
        return self.__cost

    def setsign(self, sign):
        if sign == "":
            print("不能为空")
        else:
            self.sign = sign

    def setbattery(self, battery):
        if battery < 0:
            print("别要了")
        else:
            self.__battery = battery

    def getbattery(self):
        return self.__battery

    def setsize(self, size):
        if size < 0 or size > 50:
            print("别闹")
        else:
            self.__size = size

    def getsize(self):
        return self.__size

    def setdtime(self, dtime):
        if dtime < 0:
            print("别闹")
        else:
            self.__dtime = dtime

    def getdtime(self):
        return self.__dtime

    def setintegral(self, integral):
        if integral < 0:
            print("积分不能为0")
        else:
            self.__integral = integral

    def getintegral(self):
        return self.__integral

    def showme(self):
        print('姓名', self.__name, '\n性别', self.__sex, '\n年龄', self.__age, '\n所拥有的手机剩余话费',
              self.__cost, '元！\n手机品牌', self.__sign, '\n手机电池容量', self.__battery, '%\n屏幕大小',
              self.__size, '寸\n最大待机时长', self.__dtime, '分钟\n所拥有积分：', self.__integral)


p = pphone()
p.setname(input('输入姓名'))
p.setsex(input('输入性别'))
p.setage(int(input('输入年龄')))
p.setcost(float(input('输入手机剩余话费')))
p.setsign(input('输入手机品牌'))
p.setbattery(float(input('输入电池容量')))
p.setsize(int(input('输入手机屏幕大小')))
p.setdtime(int(input('输入手机最大待机时长')))
p.setintegral(int(input('输入拥有积分')))
p.showme()
cc = p.getcost()
dd = p.getintegral()

while True:
    a = int(input('需要打电话还是发短信：（1或2）'))
    if a == 1:
        a_1 = input('输入短信内容：')
        print('短信内容为：\n', a_1)
    elif a == 2:
        a_1 = int(input('输入电话号码：'))
        a_2 = int(input('输入打多长时间：'))
        if a_1 == None:
            print('不能为空！')
        elif a_1 <= 1:
            print('电话费不够了！')
        else:
            print('电话已拨通！')
        if 0 <= a_2 <= 10:
            if dd >= a_2 * 15:
                dd -= a_2 * 15
            else:
                cc -= a_2 * 1
        elif 10 < a_2 <= 20:
            if dd >= a_2 * 39:
                dd -= a_2 * 39
            else:
                cc -= a_2 * 0.8
        else:
            if dd >= a_2 * 48:
                dd -= a_2 * 48
            else:
                cc -= a_2 * 0.65

        print('剩余话费为：', cc)
        print('剩余积分为：', dd)
