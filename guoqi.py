# -*- coding: utf-8 -*-
import turtle as t
import time  
import os  

#定义尺寸
qw, qh = 660, 440                   # 过期长宽
dt = 330/15                         # 一个小格
bx, by = -330 + dt*5, 220 - dt*5    # 大五角星（中心坐标，半径）
br, sr = dt*3, dt*1                 # 大五角星半径，小五角星半径

def draw_square(x1, y1, x2, y2):
    '起点和终点坐标'
    print('画矩形', x1, y1)
    t.up()
    t.setpos(x1, y1)    # 从左下角开始绘制
    t.up()
    t.color('red', 'red')
    t.begin_fill()
    t.fd(x2 - x1)
    t.lt(90)
    t.fd(y2 - y1)
    t.lt(90)
    t.fd(x2 - x1)
    t.lt(90)
    t.fd(y2 - y1)
    t.end_fill()

def draw_star(center_x, center_y, heading, radius):  
    '中心坐标，顶点朝向，半径'
    print('画五角星', center_x, center_y, heading, radius)   #调试信息
    t.pencolor('yellow')  
    t.tracer(False)
    # 计算顶点
    t.up()
    t.setpos(center_x, center_y)
    t.seth(heading)
    t.fd(radius)    # 移动到上顶点
    t.rt(90)
    pt1 = t.pos()
    t.circle(-radius, 360 / 5)  
    pt2 = t.pos()
    t.circle(-radius, 360 / 5)  
    pt3 = t.pos()
    t.circle(-radius, 360 / 5)  
    pt4 = t.pos()
    t.circle(-radius, 360 / 5)  
    pt5 = t.pos()
    t.down()
    t.tracer(True)
    # 画图
    t.color('yellow', 'yellow')  
    t.begin_fill()  
    t.goto(pt3)  
    t.goto(pt1)  
    t.goto(pt4)  
    t.goto(pt2)  
    t.goto(pt5)  
    t.end_fill()

def calc_s_star(xx, yy):
    '坐标格'
    t.up()
    x, y = -330 + dt*xx, 220 - dt*yy
    t.goto(x, y)
    ang = t.towards(bx, by)
    return (x, y, ang, sr)

if __name__ == "__main__":
    t.speed(8)
    draw_square(-qw/2, -qh/2, qw/2, qh/2)

    #大五角星
    draw_star(bx, by, 90, br)
    #小五角星1
    r = calc_s_star(10, 2)
    draw_star(*r)
    #小五角星2
    r = calc_s_star(12, 4)
    draw_star(*r)
    #小五角星3
    r = calc_s_star(12, 7)
    draw_star(*r)
    #小五角星4
    r = calc_s_star(10, 9)
    draw_star(*r)
    
    t.ht()
    t.done()