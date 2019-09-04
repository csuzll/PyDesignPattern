"""
抽象工厂模式
"""

import math

# 定义一个“形状”的接口，里面定义一个面积的接口方法，只有方法的定义，并没有实现体
class IShape(object):
    def Area(self):
        pass

# 定义4个图形类，都是实现IShape接口，并且每一个图形都有一个可以计算面积的方法，相当于重写接口方法
class Circle(IShape):
    def Area(self, radius):
        return math.pow(radius,2) * math.pi
 
class Rectangle(IShape):
    def Area(self, longth, width):
        return 2 * longth * width
 
class Triangle(IShape):
    def Area(self, baselong, height):
        return baselong * height/2
 
class Ellipse(IShape):
    def Area(self, long_a, short_b):
        return long_a * short_b * math.pi

# 定义一个“颜色”的接口，里面定义一个颜色名称的接口方法，只有方法的定义，并没有实现体
class IColor(object):
    def color(self):
        pass
 
# 定义3个颜色类，都是实现IColor接口，并且每一个图形都有一个可以获取颜色名称的方法，相当于重写接口方法
class Red(IColor):
    def color(self, name):
        print('我的颜色是：', name)
 
class Blue(IColor):
    def color(self, name):
        print('我的颜色是：', name)
 
class Black(IColor):
    def color(self, name):
        print('我的颜色是：', name)

# 模拟接口 (抽象工厂类，按系列划分)
class IFactory(object):
    # 定义接口的方法，只提供方法的声明，不提供方法的具体实现
    def create_shape(self):
        pass
    def create_color(self):
        pass
 
# 创建形状这一个系列的工厂
class ShapeFactory(IFactory):
    def create_shape(self, name):
        if name == 'Circle':
            return Circle()
        elif name == 'Rectangle':
            return Rectangle()
        elif name == 'Triangle':
            return Triangle()
        elif name == 'Ellipse':
            return Ellipse()
        else:
            return None
 
# 创建颜色这一个系列的工厂
class ColorFactory(IFactory):
    def create_color(self, name):
        if name == 'Red':
            return Red()
        elif name == 'Blue':
            return Blue()
        elif name == 'Black':
            return Black()
        else:
            return None

# 定义一个专门产生工厂的类 (超级工厂类，决定产生哪个类的实例)
class FactoryProducer(object):
    def get_factory(self, name):
        if name == 'Shape':
            return ShapeFactory()
        elif name == 'Color':
            return ColorFactory()
        else:
            return None

if __name__ == '__main__':
    factory_producer = FactoryProducer()
    shape_factory = factory_producer.get_factory('Shape')
    color_factory = factory_producer.get_factory('Color')
    #--------------------------------------------------------------
    circle = shape_factory.create_shape('Circle')
    circle_area = circle.Area(2)
    print(f'这是一个圆, 它的面积是：{circle_area}')
    rectangle = shape_factory.create_shape('Rectangle')
    rectangle_area = rectangle.Area(2,3)
    print(f'这是一个长方形，它的面积是：{rectangle_area}')
    triangle = shape_factory.create_shape('Triangle')
    triangle_area = triangle.Area(2,3)
    print(f'这是一个三角形，它的面积是：{triangle_area}')
    ellipse = shape_factory.create_shape('Ellipse')
    ellipse_area = ellipse.Area(3,2)
    print(f'这是一个椭圆，它的面积是：{ellipse_area}')
    #---------------------------------------------------------------
    red = color_factory.create_color('Red')
    red.color('红色')
    blue = color_factory.create_color('Blue')
    blue.color('蓝色')
    black = color_factory.create_color('Black')
    black.color('黑色')


# 缺点
"""
比如，我还要在增加一系列的材质类型（包括Stone、Wood、Plastic等）。
首先，我需要再定义一个抽象材质接口，然后定义很多的类去实现这个接口；
然后，我需要在抽象工厂接口中添加一个create_material()方法，并且还需要实现一个MaterialFactory工厂类；
最后，我还需要更改超级工厂FactoryProducer类
"""