import jieba

def count_characters_advanced(filename):
    file=open(filename,'r',encoding='utf-8').read()
    characters = {
        '贾宝玉':['宝玉','宝二爷','怡红公子'],
        '林黛玉':['黛玉','林妹妹','颦儿'],
        '薛宝钗':['宝钗','宝姑娘','蘅芜君'],
        '王熙凤':['凤姐','琏二奶奶','凤辣子'],
        '贾母':['老太太','史太君'],
        '贾政':['政老爷'],
        '王夫人':['太太'],
        '贾琏':['琏二爷'],
        '贾元春':['元春','贵妃'],
        '贾探春':['探春','三姑娘'],
        '贾惜春':['惜春','四姑娘'],
        '贾迎春':['迎春','二姑娘'],
        '史湘云':['湘云','史大姑娘'],
        '李纨':['李宫裁','珠大奶奶'],
        '秦可卿':['可卿'],
        '妙玉':[],
        '贾赦':['大老爷'],
        '邢夫人':[],
        '尤氏':['珍大奶奶'],
        '贾珍':['珍大爷'],
        '贾蓉':['蓉哥儿'],
        '薛蟠':['薛大爷'],
        '袭人':['花袭人'],
        '晴雯':[],
        '平儿':[],
        '鸳鸯':[],
        '紫鹃':[],
        '香菱':['甄英莲'],
        '刘姥姥':[]
    }

    name_map={}
    for standard_name,aliases in characters.items():
        name_map[standard_name]=standard_name
        for alias in aliases:
            name_map[alias]=standard_name

    words=jieba.lcut(file)

    counts={}
    for word in words:
        if word in name_map:
            standard_name=name_map[word]
            counts[standard_name]=counts.get(standard_name, 0) + 1

    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)

    return items

items=count_characters_advanced("《红楼梦》.txt")
for i in range(20):
    print(f"人物:{items[i][0]} 出场次数:{items[i][1]}")
