def isNum1(letter):
    try:
        letter = eval(letter)
        if type(letter) == int or type(letter) == float or type(letter) == complex:
            return True
        else:
            return False
    except:
        return False

def isNum2(letter):
    try:
        letter = eval(letter)
        if type(letter) == int:
            return "整数"
        elif type(letter) == float:
            return "浮点数"
        elif type(letter) == complex:
            return "复数"
        else:
            return False
    except:
        return False


letter=input("请输入一个字符串:")
result1 = isNum1(letter)
result2 = isNum2(letter)
if result1:
    print("该字符串属于整数、浮点数或复数其中之一")
else:
    print("该字符串不属于整数、浮点数或复数其中之一")

if result2:
    print("该字符串属于" + result2)
else:
    print("该字符串不属于整数、浮点数或复数其中之一")