#!/usr/bin/python3
"""Class Rectangle """
from models.base import base


class Rectangle(Base):
    """Defines Rectangle class
    Inherits from:
        Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private attribute"""
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Returns private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private attribute"""
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Returns private attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets private attribute"""
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Returns private attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets private attribute"""
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.height * self.width)

    def display(self):
        """Prints stdout representation of rectangle"""
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Updates the args in class"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns dict representation of class"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        """Overwrites the str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                        self.width, self.height)

