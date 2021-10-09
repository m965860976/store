'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：猜3次就睡眠 time.sleep(10)
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
import time

randint = random.randint(1, 30)  # 随机产生的数字
gold = 5000
tries = 1
while tries <= 15:
    print(randint)
    num = input("请输入一个数字")
    if num.isdigit():
        num = int(num)
        if num == randint:
            print("you win!")
            gold = gold + 3000
            print(gold)
            randint = random.randint(1, 30)
        elif num > randint:
            print("猜大了")
            gold = gold - 500
            print(gold)
            tries = tries + 1
        elif num < randint:
            print("猜小了")
            gold = gold - 500
            print(gold)
            tries = tries + 1
    else:
        print("别瞎输入")
        time.sleep(10)
else:
    print("15次了还猜不中，找个班上吧")

