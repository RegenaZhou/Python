import random
name=input("请输入名字:")
lucky=1
random.seed(7)
# 当 c 是汉字时，ord(c) 返回的是该汉字在 Unicode 字符集中的编码值
for c in name:
    lucky+=ord(c)*random.randint(1,77)
    print(ord(c),lucky)
print("幸运数字是:{}".format(lucky%777))