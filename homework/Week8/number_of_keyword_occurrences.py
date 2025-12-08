import keyword

def python_keyword_analysis(filename):
    file=open(filename, "r", encoding='utf-8').read()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        file=file.replace(ch," ")

    words=file.split()
    python_keywords=keyword.kwlist # 获取python关键字列表
    counts={}

    for word in words:
        if word in python_keywords:
            counts[word]=counts.get(word, 0) + 1

    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)

    return items

filename=input("请输入Python源程序文件名称:")
for keyword, count in python_keyword_analysis(filename):
    print(f"{keyword:<15}{count:>5}")