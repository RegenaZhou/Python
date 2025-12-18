"""
开发一个罕见词抽取程序，要求首先输入一个常用英语单词表文件，然后读入一本书的文本，检查并汇集问吧中所有没出现在英语单词表里的单词，并输出这些单词。
"""
def get_english_text(load):
    with open(load, "r", encoding='utf-8') as file:
        content = file.read().lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            content = content.replace(ch, " ")
    # print(f"英文文本\n{content}")
    return content

def get_word_list(load):
    with open(load, "r", encoding='utf-8') as file:
        content = file.read().lower()
        for ch in content:
            if not 'a'<=ch<='z':
                content = content.replace(ch, " ")
        words = content.split()
    # print(f"单词列表\n{words}")
    return words


def find_rare_words(book_content, common_words):
    book_words = book_content.split()
    rare_words = []

    for word in book_words:
        if word not in common_words and word not in rare_words:
            rare_words.append(word)

    rare_words.sort()
    return rare_words

words_load = input("请输入常用英语单词表文件路径:")
book_load = input("请输入书籍文本文件路径:")

common_words = get_word_list(words_load)
book_content = get_english_text(book_load)
rare_words = find_rare_words(book_content, common_words)

print("罕见词")
for word in rare_words:
    print(f"{word}")
