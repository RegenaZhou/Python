def get_english_text(load):
    with open(load,"r",encoding='utf-8') as file:
        content=file.read().lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            content=content.replace(ch," ")
    return content

def english_word_count(file):
    words=file.split()
    counts={}
    for word in words:
        counts[word]=counts.get(word,0)+1

    once_words=[]
    for word,count in counts.items():
        if count==1:
            once_words.append(word)

    once_words.sort()
    return once_words

load=input("请输入英文文本文件路径:")
for word in english_word_count(get_english_text(load)):
    print(f"{word}")