from turtle import *
color('red','yellow') # # 画笔红色，填充黄色
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
# done()启动事件循环并保持 Turtle 图形窗口打开
done()