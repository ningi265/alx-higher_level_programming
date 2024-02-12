#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (optional): An identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a rectangle with the given width, height, position (x, y), and optional id.
        area(self):
            Calculates and returns the area of the rectangle.
        display(self):
            Displays the rectangle using "#" characters on the console.
        __str__(self):
            Returns a string representation of the rectangle.
        update(self, *args, **kwargs):
            Updates the attributes of the rectangle. Accepts either positional arguments or keyword arguments.
        to_dictionary(self):
            Returns a dictionary representation of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle with the given width, height, position (x, y), and optional id."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute. Ensures height is an integer and > 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Displays the rectangle using "#" characters on the console."""
        for i in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle.

        Accepts either positional arguments (height, width, id, x, y) or keyword arguments.
        """
        if args:
            if len(args) > 5:
                raise ValueError("Too many arguments provided")
            if len(args) >= 1:
                self.height = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.id = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle."""
        return {
            'x': self.x,
            'y': self.y,
            'height': self.height,
            'width': self.width,
            'id': self.id,
        }

