letter=input("请输入一个大写英文字母")
blank=ord(letter)-ord('A')
for i in range(blank+1):
    print(' '*blank,end='')
    s=""
    for j in range(i):
        s+=chr(ord('A')+j)
    print(s+chr(ord('A')+i)+s[::-1])
    blank-=1