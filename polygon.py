"""
Build a Polygon Area Calculator
In this project, you will use object-oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit its methods and attributes.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should create a Rectangle class.

When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

set_width: Sets the width of the rectangle.
set_height: Sets the height of the rectangle.
get_area: Returns area ( width×height
 ).
get_perimeter: Returns perimeter  2(width+height)
 .
get_diagonal: Returns diagonal  width2+height2−−−−−−−−−−−−−−√
 .
get_picture: Returns a string that represents the shape using lines of *. The number of lines should be equal to the height and the number of * in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: Too big for picture..
get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
If an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10).

You should create a Square class that subclasses Rectangle.

When a Square object is created, it should be initialized with a single side length. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should contain the following methods:

set_width: Overrides the set_width method from the Rectangle class. It should set the width and height to the side length.
set_height: Overrides the set_height method from the Rectangle class. It should set the width and height to the side length.
set_side: Sets the height and width of the square equal to the side length.
The Square class should be able to access the Rectangle class methods.

If an instance of a Square is represented as a string, it should look like: Square(side=9).

Usage example
Example Code
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
That code should return:

Example Code
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
Tests:
Waiting:12. Rectangle(3, 6).get_diagonal() should return 6.708203932499369.
Waiting:13. Square(5).get_diagonal() should return 7.0710678118654755.
Waiting:14. An instance of the Rectangle class should have a different string representation after setting new values.
Waiting:15. An instance of the Square class should have a different string representation after setting new values by using .set_side().
Waiting:16. An instance of the Square class should have a different string representation after setting new values by using .set_width() or set_height().
Waiting:17. The .get_picture() method should return a different string representation of a Rectangle instance.
Waiting:18. The .get_picture() method should return a different string representation of a Square instance.
Waiting:19. The .get_picture() method should return the string Too big for picture. if the width or height attributes are larger than 50.
Waiting:20. Rectangle(15,10).get_amount_inside(Square(5)) should return 6.
Waiting:21. Rectangle(4,8).get_amount_inside(Rectangle(3, 6)) should return 1.
Waiting:22. Rectangle(2,3).get_amount_inside(Rectangle(3, 6)) should return 0.
"""

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def set_width(self, new_width):
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def set_height(self, new_height):
        self._height = new_height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * (self._width + self._height)

    def get_diagonal(self):
        pass
        # return square root of width squared plus height squared

    def get_picture(self):
        pass
        # return a string that represents the shape using lines of '*'
        # the number of lines should be equal to the height 
        # and the number of each '*' in each line should be equal to the width
        # there should be a new line (\n) at the end of each line.
        # if the width or height is larger than 50, this should return the string "Too big for picture."

    def get_amount_inside(self, shape):
        pass
        # returns the number of times {shape} can fit into self.shape
        # for instance, a rectangle with a width of 4 and a height of 8 could fit two squares with sides of 4.

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

class Square(Rectangle):
    def __init__(self, side):
        self._width = side
        self._height = side

    @property
    def width(self):
        super().width

    @width.setter
    def set_width(self, new_width):
        self._width = new_width
        self._height = new_width

    @property 
    def height(self):
        super.height()
    
    @height.setter
    def set_height(self, new_height):
        self._width = new_height
        self._height = new_height

    @property
    def side(self):
        return self._width

    @side.setter
    def set_side(self, new_side):
        self._height = new_side
        self._width = new_side

    def __str__(self):
        return f"Square(side={self._width})"

    
rectangle = Rectangle(5, 10)
square = Square(4)
print(rectangle)
print(square)