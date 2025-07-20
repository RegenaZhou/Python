f=open(r".\data1.txt",'r',encoding='utf-8')
content=f.read()
print(content)
f.close()

# with open(r".\data1.txt","r",encoding="utf-8") as f:
#     lines=f.readlines()
#     for line in lines:
#         print(line)