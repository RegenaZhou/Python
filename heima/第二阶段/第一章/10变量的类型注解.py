# import random
# print(random.randint(1,10)) # ctrl+P 提示类型
import json
import random

# 基础数据类型注解
var_1:int=10
var_2:str="itheima"
var_3:bool=True

# 类对象类型注解
class Student:
    pass
stu:Student=Student()

# 基础容器类型注解
my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_dict:dict={"itheima":666,"heihei":77}

# 容器类型详细注解
my_list1:list[int]=[1,2,3]
my_tuple1:tuple[int,str,bool]=(1,"itheima",True)
my_dict1:dict[str,int]={"itheima":666}

# 注意：元组类型设置类型详细注解，需要将每一个元素都标记出来
# 字典类型设置类型注解，需要2个类型，第一个是key第二个是value

# 在注释中进行类型注解
var_11=random.randint(1,10)  #type:int
# son.loads() 是 Python 内置 json 模块中的一个函数，
# 用于将 JSON 格式的字符串（String）解码（反序列化）为对应的 Python 对象。
var_22=json.loads('{"name":"zhangsan"}')  #type:dict[str,str]
def func():
    return 10
var_33=func()  #type:int

# 类型注解的限制
# 类型注解只是提示性的，并非决定性的。数据类型和注解类型无法对应也不会导致错误
var_4:int="itheima"
var_5:str=123
print(type(var_5)) # <class 'int'>
