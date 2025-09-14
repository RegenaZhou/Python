for i in range(1,10): # 1~9
    for j in range(1,i+1): # 1~i
        print("{}*{}={:<2}".format(i,j,i*j),end=' ')
    print('')