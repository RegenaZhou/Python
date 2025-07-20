# 结合input、字典、if判断，做一个查询流行语含义的电子词典程序
slang_dict={"数智化":"数字化与智能化的结合，强调在数字化基础上的更高诉求。",
            "智能向善":"指利用智能技术促进社会的积极发展。"}
slang_dict["未来产业"]="指面向未来的新兴产业，强调创新和可持续发展。"
slang_dict["水灵灵地"]="形容事物清新、灵动的状态。"
slang_dict["班味"]="指某个班级或团队特有的氛围和文化。"
slang_dict["松弛感"]="形容一种轻松、自在的状态。"
slang_dict["银发力量"]="强调老年人在社会中的积极作用和影响力。"
slang_dict["小孩哥/小孩姐"]="指年轻人对儿童的亲切称呼，体现对年轻一代的关注。"
slang_dict["city不city"]="探讨城市化进程中的各种现象和问题。"
slang_dict["硬控"]="指在某些领域采取严格控制的措施。"

query=input("请输入您要查询的流行语：")
if query in slang_dict.keys():
    print("您查询的"+query+"含义如下")
    print(slang_dict[query])
else:
    print("您查询的流行语暂未收录。")
    print("当前本词典收录词条数为："+str(len(slang_dict))+"条。")