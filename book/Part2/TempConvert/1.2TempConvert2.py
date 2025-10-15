def TempConverter(TempStr):
    if TempStr[-1] in ['F', 'f']:
        C = (eval(TempStr[0:-1]) - 32) / 1.8
        return "转化后的温度是{:.2f}F".format(C)
    elif TempStr[-1] in ['C', 'c']:
        F = 1.8 * eval(TempStr[0:-1]) + 32
        return "转化后的温度是{:.2f}C".format(F)
    else:
        return "输入格式错误"

value=input("请输入带有符号的温度值:")
print(TempConverter(value))