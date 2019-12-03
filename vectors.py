import PyQt5


class Vector:
    def draw(self):
        pass

    def selected(self): # 被选中时的处理逻辑
        # 找几个关键点，画出正方形表示选中状态
        pass

    def unselected(self):   # 失去选中状态时的处理逻辑
        # 取到选中状态时画的正方形
        pass


class Line(Vector):
    pass


class Rectangle(Vector):
    pass


class Square(Rectangle):
    pass


class Ellipse(Vector):
    pass


class Circle(Ellipse):
    pass


class FivePointedStar(Vector):
    pass
