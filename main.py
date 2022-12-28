# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt

def PointInFlat(xa, ya, xb, yb, xc, yc, x, y):
    First = (xa - x) * (yb - ya) -  (xb-xa) * (ya - y)
    Second = (xb - x) * (yc - yb) - (xc - xb) * (yb - y)
    Third = (xc - x) * (ya - yc) - (xa - xc) * (yc - y)
    if ((First <= 0) and (Second <= 0) and (Third <= 0)) or((First >= 0) and (Second >= 0) and (Third >= 0)):
        return True
    else:
        return False

def shading(x1,y1,x2,y2,x3,y3,xmin,xmax,ymin,ymax):
    arr_t=[]
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if PointInFlat(x1,y1,x2,y2,x3,y3, x, y):
                arr_t.append((x, y))
    return arr_t
if __name__ == '__main__':
    fig = plt.figure(figsize=(30, 15))
    ax = fig.add_subplot(121)
    print('Введите две коордианты первой вершины треугольника через пробел')
    x1,y1=map(int,input().split())
    print('Введите две коордианты второй вершины треугольника через пробел')
    x2,y2=map(int,input().split())
    print('Введите две коордианты третьей вершины треугольника через пробел')
    x3,y3=map(int,input().split())
    xmax=max(x1,x2,x3)
    xmin=min(x1,x2,x3)
    ymin=min(y1,y2,y3)
    ymax=max(y1,y2,y3)
    arr_point = shading(x1,y1,x2,y2,x3,y3,xmin,xmax,ymin,ymax)
    for point in arr_point:
        ax.plot(point[0], point[1], 'ro')
    ax.set_xticks(range(xmin,xmax+1))
    ax.set_yticks(range(ymin,ymax+1))
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
