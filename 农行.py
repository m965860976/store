import random

print("*****************************")
print("*    中国农业银行账户管理系统    *")
print("*****************************")
print("*          1、开户           *")
print("*          2、存钱           *")
print("*          3、取钱           *")
print("*          4、转账           *")
print("*          5、查询           *")
print("*          6、再见           *")
print("*****************************")

# 开户逻辑
bank = {}  # 空的银行账户数据库
# 'Frank': {'account': 10936377, 'password': '123', 'country': '中国', 'province': '山东', 'street': '蓝翔', 'door': '001'},
bank_name = "中国农业银行沙河分行"


# 传入参数添加到字典里面
def bank_add(account, username, password, account_type, country, province, street, door):
    if username in bank:  # 说明用户已存在
        return 2
    elif len(bank) >= 100:
        return 3
    else:
        bank[username] = {
            "account": account,
            "password": password,
            "account_type": account_type,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1


# 开户
def useradd():
    account = random.randint(10000000, 99999999)
    username = input("请输入您的用户名")
    password = input("请输入您的用户密码")
    account_type = input("请输入您的账户类型")
    if len(password) == 6:
        print("下面请输入你的详细地址")
        country = input("\t\t请输入您的国家")
        province = input("\t\t请输入您的省份")
        street = input("\t\t请输入您的街道")
        door = input("\t\t请输入您的门牌号")
        add = bank_add(account, username, password, account_type, country, province, street, door)
        if add == 3:
            print("数据库已满请到其他银行开户")
        elif add == 2:
            print("请输入其他用户名")
        elif add == 1:
            print("开户成功,下面是你的详细信息")
            info = '''
                        ------------个人信息------------
                        用户名:%s
                        账号：%s
                        密码：*****
                        账户类型: %s
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                        余额：%s
                        开户行名称：%s
                    '''
            # 每个元素都可传入%
            print(info % (
                username, account, account_type, country, province, street, door, bank[username]["money"], bank_name))
    else:
        print("密码必须为6位数")


# 存钱
def bank_saving():
    username = input("请输入您的用户名：")
    if username in bank:
        smoney = int(input("请输入您要存款的金额："))
        bank[username]["money"] = smoney + bank[username]["money"]
    else:
        print("没有此用户名")


# 取款
def bank_take():
    username = input("请输入您的用户名：")
    if username in bank:
        password = input("请输入您的密码：")
        if password == bank[username]["password"]:
            tmoney = int(input("请输入您要取金额："))
            if bank[username]["money"] > tmoney:
                bank[username]["money"] = bank[username]["money"] - tmoney
                print("取款成功")
                return 0
            else:
                print("余额不足")
                return 3
        else:
            print("密码输入错误")
            return 2
    else:
        print("用户名输入错误")
        return 1


# 转账
def bank_debit():
    sav_username = input("请输入要转入的用户名：")
    tak_username = input("请输入要转出的用户名：")
    account_type = input("请输入要转出账户的账户类型：")
    if sav_username and tak_username in bank:
        tak_password = input("请输入要转出账号的密码：")
        if tak_password == bank[tak_username]["password"]:
            tak_money = int(input("请输入要转出的金额："))
            if account_type == "1类" and tak_money <= 50000:
                if tak_money <= bank[tak_username]["money"]:
                    bank[tak_username]["money"] = bank[tak_username]["money"] - tak_money
                    bank[sav_username]["money"] = bank[sav_username]["money"] + tak_money
                    print("转账成功")
                    return 0
                else:
                    print("余额不足")
                    return 3
            elif account_type == "2类" and tak_money <= 20000:
                if tak_money <= bank[tak_username]["money"]:
                    bank[tak_username]["money"] = bank[tak_username]["money"] - tak_money
                    bank[sav_username]["money"] = bank[sav_username]["money"] + tak_money
                    print("转账成功")
                    return 0
                else:
                    print("余额不足")
                    return 3
            else:
                print("转账金额超出转账额度")
        else:
            print("密码输入错误")
            return 2
    else:
        print("用户名输入错误")
        return 1


# 查询
def bank_inquire():
    inq_username = input("请输入要查询的用户名：")
    if inq_username in bank:
        inq_password = input("请输入要查询账号的密码：")
        if inq_password == bank[inq_username]["password"]:
            print(bank[inq_username])
        else:
            print("密码错误")
    else:
        print("用户名错误")


while 1:
    index = int(input("请输入您的操作"))
    if index == 1:
        print("1、开户")
        useradd()
        print(bank)
    elif index == 2:
        print("2、存钱")
        bank_saving()
        print(bank)
    elif index == 3:
        print("3、取钱")
        bank_take()
        print(bank)
    elif index == 4:
        print("4、转账")
        bank_debit()
        print(bank)
    elif index == 5:
        print("5、查询")
        bank_inquire()
    elif index == 6:
        print("退出系统")
        break
