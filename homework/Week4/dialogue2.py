def tostring(load):
    with open(load, 'r', encoding='utf-8') as file:  # 显式指定编码
        for line in file:
            print(line, end='')  # 避免 print 添加额外的换行

tostring('leiyu.txt')
tostring('xiangyuexingqier.txt')