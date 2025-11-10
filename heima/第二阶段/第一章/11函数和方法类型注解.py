# def 函数方法名(形参:类型,......,形参:类型) -> 返回值类型:
#     pass

# 对形参进行类型注解
def add(x:int,y:int):
    return x+y

# 对返回值进行类型注解
def func(data:list) -> list:
    return data

# 函数中类型注解只是提示性的，而非决定性的
print(type(func(1))) # <class 'int'>
