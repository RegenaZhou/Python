def duplicate_element_determination(liebiao):
    flag=False
    for i in liebiao:
        if liebiao.count(i)>1:
            flag=True
            break

    return flag

liebiao=input("请输入你要判断的列表(元素间用空格分割):").split()
if duplicate_element_determination(liebiao)==True:
    print("列表中有重复元素")
else:
    print("列表中无重复元素")