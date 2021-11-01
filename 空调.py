class Airc:
    __sign = ""
    __price = ""

    def setsign(self, sign):
        self.__sign = sign

    def getsign(self):
        return self.__sign

    def setprice(self, price):
        if price < 0:
            print("真的吗？？")
        else:
            self.__price = price

    def getprice(self):
        return self.__price

    def openairc(self):
        print(self.__sign, "空调开机了...")

    def closeairc(self, minute):
        print(self.__sign, "空调将在", minute, "分钟后自动关闭...")


a = Airc()

a.setsign("格力")
a.setprice(5000)
a.openairc()
a.closeairc(5)
