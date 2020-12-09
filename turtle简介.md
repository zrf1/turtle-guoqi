# 简介

import turtle（内置标准库）。所有函数都可以直接调用，函数大多有简称或多个名称

* 内置标准库，海龟绘图很适合用来引导孩子学习编程。
* 请想象绘图区有一只机器海龟，起始位置在 x-y 平面的 (0, 0) 点

## turtle需调用本地gui资源
* jupyterhub无法远程创建 tkinter.Canvas 画布，不能在线运行。
* 但本地的jupyter notebook可以，但不能交互式画图。
* 注意画图后要加turtle.mainloop()，否则会报错。


# 相关文档

https://docs.python.org/zh-cn/3/library/turtle.html

https://blog.csdn.net/sandalphon4869/article/details/99443949

https://cloud.tencent.com/developer/section/1372423

## 官方自带了一些演示效果
> python -m turtledemo

# 画布(canvas)

## 基本设置
turtle.setup(width=0.5, height=0.75, startx=None, starty=None)

turtle.screensize(canvwidth=None, canvheight=None, bg=None)

## 画布控制
turtle.clear()   清空turtle窗口，但是turtle的位置和状态不会改变

turtle.reset()   清空窗口，重置turtle状态为起始状态

turtle.undo()    撤销上一个turtle动作

screen.bgpic()   设置背景

## 绘图控制
turtle.tracer()       启用/禁用海龟动画并设置刷新图形的延迟时间

turtle.tracert(False)   0 一次画完，n每个n次刷新屏幕一次

turtle.update()       在禁用刷新时，刷新屏幕一次

turtle.mainloop()

turtle.done()

# 画笔(Pen)
原点在中心，x/y轴，初始朝x轴正方向

## 画笔设置
turtle.pensize()     width()     设置画笔粗细

turtle.pencolor()              设置画笔颜色

turtle.speed()                画画速度，"fastest": 0 最快，"fast": 10 快，"slowest": 1 最慢

## 画笔运动
turtle.pendown()     pd()       移动时绘制图形，缺省时也为绘制

turtle.penup()       pu()      提起笔移动，不绘制图形，用于另起一个地方绘制

setx( )                    将当前x轴移动到指定位置

sety( )                    将当前y轴移动到指定位置

setheading(angle)     seth()   设置当前朝向为angle角度

home()                    设置当前画笔位置为原点，朝向东。

turtle.goto(x,y)   setpos() setposition()     将画笔移动到坐标为x,y的位置

turtle.right(degree)      rt()    顺时针移动degree°

turtle.left(degree)      lt()     逆时针移动degree°

turtle.forward(distance)    fd()    向当前画笔方向移动distance像素长度

turtle.backward(distance)   bk()    向当前画笔相反方向移动distance像素长度

turtle.circle()                画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆


# 填充颜色

turtle.fillcolor(colorstring)   绘制图形的填充颜色

turtle.color(color1, color2)    同时设置pencolor=color1, fillcolor=color2

turtle.filling()         返回当前是否在填充状态

turtle.begin_fill()     准备开始填充图形

turtle.end_fill()       填充完成

# 其他图形

dot(r) 绘制一个指定直径和颜色的圆点

write(s [,font=("font-name",font_size,"font_type")]) 写文本本内容，font是字体的参数，分别为字体名称，大小和类型；font为可选项，font参数也是可选项

# turtle控制
turtle.hideturtle()   ht()  隐藏画笔的turtle形状

turtle.showturtle()   st() 显示画笔的turtle形状

turtle.isvisible()   返回当前turtle是否可见

shape()   设置画笔形状，"arrow", "turtle", "circle", "square", "triangle", "classic"

stamp()   在当前位置画turtle形状


# 全局控制

## 事件响应

onclick() 当鼠标点击

onrelease() 当鼠标释放

ondrag() 当鼠标拖动

调试用，从背景找坐标点

listen() 监听

onkey() | onkeyrelease() 当键盘按下并释放

onkeypress() 当键盘按下

onclick() | onscreenclick() 当点击屏幕


# 简单示例：画正方形


```python
from turtle import *

for x in range(1,5):
	fd(50)
	left(90)
mainloop()
```
