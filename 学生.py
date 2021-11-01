class student:
    __name = ""
    __age = 0

    def setname(self, name):
        if name == "":
            print("不能为空")
        else:
            self.__name = name

    def getname(self):
        return self.__name

    def setage(self, age):
        if age > 30 or age < 10:
            print("者这不属于你")
        else:
            self.__age = age

    def getage(self):
        return self.__age

    def showme(self):
        print("大家好，我叫", self.__name, "今年", self.__age, "岁了")

    def compare(self, compare):
        if self.__age > compare:
            print("我比同桌大", self.__age - compare, "岁")
        elif self.__age < compare:
            print("我比同桌小", compare - self.__age, "岁")
        elif self.__age == compare:
            print("我和同桌一样大")


s = student()
s.setname("法外狂徒")
s.setage(25)
s.compare(20)
s.showme()
