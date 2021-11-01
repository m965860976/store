class cup:
    __high = 0
    __capacity = 0
    __color = ""
    __material = ""

    def sethigh(self, high):
        if high > 50 or high < 0:
            print("别瞎搞")
        else:
            self.__high = high

    def gethigh(self):
        return self.__high

    def setcapacity(self, capacity):
        if capacity < 0 or capacity > 2:
            print("这是杯子么")
        else:
            self.__capacity = capacity

    def getcapacity(self):
        return self.__capacity

    def setcolor(self, color):
        self.__color = color

    def getcolor(self):
        return self.__color

    def setmaterial(self, material):
        self.__material = material

    def getmaterial(self):
        return self.__material

    def deliquid(self):
        print("一个高", self.__high, "厘米",
              "容积为", self.__capacity, "升",
              "颜色为", self.__color,
              "材质为", self.__material, "的杯子能存放液体")


c = cup()
c.sethigh(30)
c.setcapacity(1)
c.setcolor("蓝色")
c.setmaterial("不锈钢")
c.deliquid()
