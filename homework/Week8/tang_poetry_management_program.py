tang_poems = {
    "《静夜思》":{
        "author":"李白",
        "content":"床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。"},
    "《春晓》": {
        "author":"孟浩然",
        "content":"春眠不觉晓，\n处处闻啼鸟。\n夜来风雨声，\n花落知多少。"},
    "《登鹳雀楼》":{
        "author":"王之涣",
        "content":"白日依山尽，\n黄河入海流。\n欲穷千里目，\n更上一层楼。"}
}


def list_poem():
    if not tang_poems:
        print("唐诗库为空")
        return

    print("\n====== 唐诗列表 ======")
    for title in tang_poems.keys():
        print(title)


def display_poem(title):
    if title in tang_poems:
        poem = tang_poems[title]
        print(f"\n{title}")
        print(f"作者:{poem['author']}")
        print(poem['content'])
        print()


def add_poem():
    print("\n====== 添加唐诗 ======")
    title=input("请输入诗名(格式:《诗名》):")

    if title in tang_poems:
        print("该诗名已存在")
        return

    author=input("请输入作者:")
    print("请主句输入诗歌内容(输入空行结束):")
    poem_lines = []
    while True:
        line=input()
        if line == "":
            break
        poem_lines.append(line)

    tang_poems[title] = {
        "author": author,
        "content": "\n".join(poem_lines)
    }
    print(f"唐诗{title}已添加成功")


def delete_poem():
    print("\n====== 删除唐诗 ======")
    title=input("请输入要删除的诗名(格式:《诗名》):")

    if title in tang_poems:
        del tang_poems[title]
        print(f"唐诗{title}已删除成功")
    else:
        print("未找到该诗名")


def find_poem():
    print("\n====== 查找唐诗 ======")
    title=input("请输入诗名(格式:《诗名》):")

    found = False
    if title in tang_poems:
        display_poem(title)
    else:
        print("未找到该诗名")


def menu():
    print("\n===== 唐诗管理程序 =====")
    print("1.list  列出所有唐诗")
    print("2.add   添加一首唐诗")
    print("3.del   删除一首唐诗")
    print("4.find  根据诗名查找唐诗")
    print("5.exit  退出程序")
    print("=" * 22)


while True:
    menu()
    choice=int(input("请输入你要选择的功能(数字):"))

    if choice == 1:
        list_poem()
    elif choice == 2:
        add_poem()
    elif choice == 3:
        delete_poem()
    elif choice == 4:
        find_poem()
    elif choice == 5:
        print("程序已成功退出")
        break
    else:
        print("请重新输入")