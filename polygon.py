import math 

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    def set_width(self, new_width):
        self.width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        result = math.sqrt(self._width**2 + self._height**2)
        return result
        

    def get_picture(self):
        if (self._width > 50) or (self._height > 50):
            return f"Too big for picture."
        picture = ''
        for i in range(0, self._height):
            for j in range(0, self._width):
                picture += '*'
            picture += f'\n'
        return picture

    def get_amount_inside(self, shape):
        bigger = self.get_area()
        smaller = shape.get_area()
        result = int(bigger / smaller)
        return result

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    @property
    def width(self):
        super().width

    @width.setter
    def width(self, new_width):
        self._width = new_width
        self._height = new_width

    @property 
    def height(self):
        super.height()
    
    @height.setter
    def height(self, new_height):
        self._width = new_height
        self._height = new_height

    @property
    def side(self):
        return self._width

    @side.setter
    def side(self, new_side):
        self._height = new_side
        self._width = new_side

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side

    def __str__(self):
        return f"Square(side={self._width})"
