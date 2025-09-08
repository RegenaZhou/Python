currency=input("请输入带有符号的货币值（人民币RMB，美元USB）:")
# str.upper(currency[-3:])将后3位全部转化为大写字母
if str.upper(currency[-3:]) in ["RMB"]:
    USB=eval(currency[:-3])/6
    print("转化后的美元为:{:.2f}USB".format(USB))
elif str.upper(currency[-3:]) in ["USB"]:
    RMB=eval(currency[:-3])*6
    print("转化后的人民币为:{:.2f}RMB".format(RMB))
else:
    print("输入格式错误")