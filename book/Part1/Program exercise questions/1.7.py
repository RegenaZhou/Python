# 全部导入 代码更简洁，不需要重复写模块名前缀
from turtle import *
fillcolor("red")
begin_fill() # 开始填充模式
while True:
    forward(200)
    right(144)
    """
    检查海龟是否回到了起始位置附近：
    pos() 返回海龟当前的坐标(x, y)
    abs(pos()) 计算当前位置到原点(0,0)的距离
    <1 表示如果距离小于1个像素，就认为海龟已经回到了起点"""
    if abs(pos())<1:
        break
end_fill()