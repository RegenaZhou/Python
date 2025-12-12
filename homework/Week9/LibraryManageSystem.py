class Book:
    def __init__(self, book_id, title, author, isbn, total_copies=1):
        self.book_id = book_id  # 书籍ID
        self.title = title  # 书名
        self.author = author  # 作者
        self.isbn = isbn  # ISBN
        self.total_copies = total_copies  # 总数量
        self.available_copies = total_copies  # 可借数量

    def borrow_book(self):
        if self.available_copies != 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies == self.total_copies:
            return False
        else:
            self.available_copies += 1
            return True

    def __str__(self):
        return (f"ID: {self.book_id:<4}, 书名: {self.title:20}, 作者: {self.author:15}, "
                f"总数量: {self.total_copies} 本, 可借阅数量: {self.available_copies} 本")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def borrow_book(self, book_id):
        if book_id in self.books and self.books[book_id].borrow_book():
            print(f"书籍《{self.books[book_id].title}》借阅成功")
            return True
        else:
            print(f"书籍《{self.books[book_id].title}》已被借完，暂时无法借阅")
            return False

    def return_book(self, book_id):
        if book_id in self.books and self.books[book_id].return_book():
            print(f"书籍《{self.books[book_id].title}》归还成功")
            return True
        else:
            print(f"书籍归还出错")
            return False

    def list_books(self):
        for book in self.books.values():
            print(book)


library = Library()

library.add_book(Book(1, "Python编程从入门到实践", "Eric Matthes", "9787115428028", 3))
library.add_book(Book(2, "数据结构与算法", "Mark Allen Weiss", "9787111407010", 2))
library.add_book(Book(3, "深入理解计算机系统", "Randal E. Bryant", "9787111544937", 1))

while True:
    print("\n===== 图书借阅管理系统 =====")
    print("1. 查看所有图书")
    print("2. 借阅图书")
    print("3. 归还图书")
    print("4. 添加新书")
    print("0. 退出系统")

    choice = input("请选择操作: ")

    if choice == '1':
        library.list_books()

    elif choice == '2':
        book_id = int(input("请输入要借阅的图书ID: "))
        library.borrow_book(book_id)

    elif choice == '3':
        book_id = int(input("请输入要归还的图书ID: "))
        library.return_book(book_id)

    elif choice == '4':
        book_id = int(input("请输入图书ID: "))
        title = input("请输入书名: ")
        author = input("请输入作者: ")
        isbn = input("请输入ISBN: ")
        total_copies = int(input("请输入总数量: "))

        new_book = Book(book_id, title, author, isbn, total_copies)
        library.add_book(new_book)
        print(f"成功添加图书《{title}》")

    elif choice == '0':
        print("谢谢使用，再见！")
        break

    else:
        print("无效选择，请重新输入")
