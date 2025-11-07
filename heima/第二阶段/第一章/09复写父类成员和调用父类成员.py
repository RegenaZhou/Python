# 在子类中，如何调用父类成员
# 方式1：
# 调用父类成员
# 使用成员变量：父类名.成员变量
# 使用成员方法：父类名.成员方法(self)
#
# 方式2：
# 使用super()调用父类成员
# 使用成员变量：super().成员变量
# 使用成员方法：super().成员方法()
#
# 注意：只可以在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写的

class Phone:
    IMEI=None         # 序列号
    producer="ITCAST" # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")


class MyPhone(Phone):
    producer="ITHEIMA"  # 复写父类的成员属性

    # 复写父类的成员方法
    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # print("使用5g网络进行通话")
        # 方式1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")


phone=MyPhone()
phone.call_by_5g()
print(phone.IMEI)