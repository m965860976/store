class computer:
    __size = 0.0
    __price = 0
    __cpu = ""
    __inmemory = 0
    __btime = 0

    def setsize(self, size):
        if size < 0 or size > 50:
            print("你家电脑这大？")
        else:
            self.__size = size

    def getsize(self):
        return self.__size

    def setprice(self,price):
        if price <0 :
            print("真的吗？那我不客气了")
        else:
            self.__price=price

    def getprice(self):
        return self.__price

    def setcpu(self,cpu):
        self.__cpu=cpu

    def getcpu(self):
        return self.__cpu

    def setinmemory(self,inmemory):
        if inmemory<0:
            print("开玩笑呢????")
        else:
            self.__inmemory=inmemory

    def getinmemory(self):
        return self.__inmemory

    def setbtime(self,btime):
        if btime<0:
            print("砸了吧，没啥用")
        else:
            self.__btime=btime

    def getbtime(self):
        return self.__btime

    def write(self):
        print("小明已经打了",self.__btime,"小时的字")

    def playgame(self,game):
        print("小王正在用",self.__price,"元",
              "CPU为",self.__cpu,
              "内存为",self.__inmemory,"T的电脑玩",game)

    def watch(self,movie):
        print("小李正在用",self.__size,"英寸的电脑看",movie)


d = computer()
d.setsize(15.5)
d.setprice(10000)
d.setcpu("3090")
d.setinmemory(1)
d.setbtime(24)

d.write()
d.playgame("LOL")
d.watch("长津湖")




