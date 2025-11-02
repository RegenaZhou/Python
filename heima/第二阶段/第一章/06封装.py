# 私有的成员变量和私有的成员方法命名均以两个下划线__开头
# 私有成员的额访问限制：类对象无法访问私有成员 类中的其它成员可以访问私有成员

class Phone:

    __current__voltage=0.5   #当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current__voltage>=1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")

phone=Phone()
# phone.__keep_single_core()
# print(phone.__current__voltage)
phone.call_by_5g()
