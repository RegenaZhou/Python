class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x  # 左下角x坐标
        self.y = y  # 左下角y坐标
        self.width = width
        self.height = height


def rect_in_circle(circle, rect):
    # 1.检查圆心是否在矩形内
    if rect.x <= circle.x <= rect.x + rect.width and rect.y <= circle.y <= rect.y + rect.height:
        return True

    # 2.检查矩形的4个顶点是否在圆形内
    # 矩形的四个顶点
    corners = [
        (rect.x, rect.y),  # 左下角
        (rect.x + rect.width, rect.y),  # 右下角
        (rect.x + rect.width, rect.y + rect.height),  # 右上角
        (rect.x, rect.y + rect.height)  # 左上角
    ]

    for corner in corners:
        distance = ((corner[0] - circle.x) ** 2 + (corner[1] - circle.y) ** 2) ** 0.5
        if distance <= circle.radius:
            return True

    # 3.检查矩形的边是否与圆相交
    # 检查矩形的左右两边是否与圆相交
    distance = min(abs(circle.x - rect.x), abs(circle.x - (rect.x + rect.width)))
    if distance <= circle.radius:
        return True

    # 检查矩形的上下两边是否与圆相交
    distance = min(abs(circle.y - rect.y), abs(circle.y - (rect.y + rect.height)))
    if distance <= circle.radius:
        return True

    return False


x = int(input("请输入圆心的x坐标:"))
y = int(input("请输入圆心的y坐标:"))
r = int(input("请输入圆的半径:"))
my_circle = Circle(x, y, r)

x = int(input("请输入矩形左下角的x坐标:"))
y = int(input("请输入矩形左下角的y坐标:"))
w = int(input("请输入矩形的宽度:"))
h = int(input("请输入矩形的高度:"))
my_rect = Rectangle(x, y, w, h)

if rect_in_circle(my_circle, my_rect):
    print("矩形与圆相交")
else:
    print("矩形与圆不相交")
