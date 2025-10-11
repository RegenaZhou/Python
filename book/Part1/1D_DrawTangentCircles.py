"""Turtle库的工作机制
单画布设计：Turtle图形库默认在一个单独的图形窗口中工作，
所有绘图命令都会在这个窗口中执行。

累积绘制：Turtle的绘图是累积的，意味着每个绘图命令都会
在前一个命令的基础上添加图形，而不是替换或创建新的画布。

连续绘制：Turtle保持一个"笔"的位置和状态，每个绘图命令
都从当前位置开始，绘制完成后笔会停留在新的位置。"""
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)
