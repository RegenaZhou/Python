dic1={1:"Mon",2:"Tues",3:"Wed",4:"Thur",5:"Fri",6:"Sat",7:"Sun"}
print(f"键列表{list(dic1.keys())}")
print(f"值列表{list(dic1.values())}")
print(f"键值列表{list(dic1.items())}")

dic2=dict()
for item in dic1.items():
    dic2[item[1]]=item[0]
print(f"键列表{list(dic2.keys())}")
print(f"值列表{list(dic2.values())}")
print(f"键值列表{list(dic2.items())}")