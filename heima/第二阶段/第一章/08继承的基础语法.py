# 单继承
class Phone:
    IMEI=None     # 序列号
    producer="ITCAST" # 厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id="10001" #面部识别ID

    def call_by_5g(self):
        print("2022年新功能，5g通话")

phone=Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 多继承
class NFCReader:
    nfc_type="第五代"
    producer="HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type="红外遥控"

    def control(self):
        print("红外遥控开启了")


# pass是占位语句，用来保证函数（方法）或者定义的完整性，表示无内容，空的意思
class MyPhone(Phone,NFCReader,RemoteControl):
    pass


phone=MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

# 单继承：一个类继承另一个类
# 多继承：一个类继承多个类，按照顺序从左向右依次继承
# 多继承中：如果父类有同名方法或属性，先继承的优先级高于后继承
# if成员属性或者成员方法同名，按照左边的先来
print(phone.producer)