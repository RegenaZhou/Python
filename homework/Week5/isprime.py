import math
# 试除法
def isprime1(num):
    if type(num) is not int:
        return False
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True

# 埃氏筛
def isprime2(num):
    if type(num) is not int:
        return False
    if num < 2:
        return False

    isPrime = [True] * (num + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2,int(math.sqrt(num))+1):
        if isPrime[i]:
            for j in range(i*i,num+1,i):
                isPrime[j]=False

    return isPrime[num]

# 线性筛
def isprime3(num):
    if type(num) is not int:
        return False
    if num < 2:
        return False

    isPrime = [True] * (num + 1)
    isPrime[0] = isPrime[1] = False
    primes=[]
    for i in range(2,num+1):
        if isPrime[i]:
            primes.append(i)
            j=0
            while j<len(primes) and i*primes[j]<=num:
                isPrime[i*primes[j]]=False
                if i % primes[j] == 0:
                    break
                j+=1

    return isPrime[num]

num=eval(input("请输入你要判断的数:"))

if isprime1(num):
    print(f"用试除法得{num}是质数")
else:
    print(f"用试除法得{num}不是质数")

if isprime2(num):
    print(f"用埃氏筛得{num}是质数")
else:
    print(f"用埃氏筛得{num}不是质数")

if isprime3(num):
    print(f"用线性筛得{num}是质数")
else:
    print(f"用线性筛得{num}不是质数")