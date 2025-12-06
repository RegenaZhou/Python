import jieba

def get_english_text(load):
    file=open(load,"r").read().lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        file=file.replace(ch,"")

    return file

def english_character_analysis(file):
    words=file.split()
    counts={}
    for word in words:
        counts[word]=counts.get(word,0)+1

    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)

    return items

def get_chinese_text(load):
    file=open(load,"r",encoding='utf-8').read()

    return file

def chinese_character_analysis(file):
    words=jieba.lcut(file)
    counts={}
    for word in words:
        if len(word)==1: # 排除单个字符
            continue
        else:
            counts[word]=counts.get(word,0)+1

    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)

    return items

load1=input("请输入你要分词的英文文本路径:") # E:/Pycharmproject/homework/Week4/xiangyuexingqier.txt
for character in english_character_analysis(get_english_text(load1)):
    word,count=character
    print(f"{word:<17}{count:>5}")

load2=input("请输入你要分词的中文文本路径:") # E:/Pycharmproject/homework/Week4/leiyu.txt
for character in chinese_character_analysis(get_chinese_text(load2)):
    word,count=character
    print(f"{word:<5}{count:>5}")
