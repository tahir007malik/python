class Rectangle:
    def draw(self):
        print('drawing a rectangle')
    
    def get_area(self, length, breadth):
        return length * breadth

class Circle:
    def draw(self):
        print('drawing a circle')
    
    def get_area(self, radius):
        return 3.14159 * radius * radius

class Triangle:
    def draw(self):
        print('drawing a triangle')

t = Triangle()
t.draw()