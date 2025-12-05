import random

def random_password():
    optional=[]
    for i in range(26):
        optional.append(chr(i + 65))
        optional.append(chr(i + 97))
        if i<10:
            optional.append(chr(i + 48))

    password=""
    for j in range(8):
        password+=optional[random.randint(0,len(optional)-1)]

    return password

passwords=[]
for i in range(10):
    passwords.append(random_password())

for i in range(10):
    print(f"生成的第{i+1}个密码是:{passwords[i]}")