#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle  # Importing the Rectangle class from the alx.rectangle module


class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle where all sides are of equal length.
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size (length of each side) of the square.
            x (int, optional): The x-coordinate of the top-left corner of the square. Default is 0.
            y (int, optional): The y-coordinate of the top-left corner of the square. Default is 0.
            id (any, optional): An identifier for the square. Default is None.
        """
        super().__init__(size, size, x, y, id)  

    @property
    def size(self):
        """
        Getter property for the size (length of each side) of the square.

        Returns:
            int: The size of the square.
        """
        return self.width  # Width is used to represent the size of the square

    @size.setter
    def size(self, value):
        """
        Setter property for the size (length of each side) of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value  # Update both width and height to maintain square shape
        self.height = value

    def __str__(self):
        """
        String representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"  # Display type, ID, position, and size

    def update(self, *args, **kwargs):
        """
        Update the properties of the square.

        Args:
            *args: Positional arguments for ID, size, x, and y in that order.
            **kwargs: Keyword arguments for updating specific properties (id, size, x, y).
        """
        if args:  # If positional arguments are provided
            if len(args) >= 1:
                self.id = args[0]  # Update ID if provided
            if len(args) >= 2:
                self.size = args[1]  # Update size if provided
            if len(args) >= 3:
                self.x = args[2]  # Update x-coordinate if provided
            if len(args) >= 4:
                self.y = args[3]  # Update y-coordinate if provided
        else:  # If keyword arguments are provided
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Convert the square object to a dictionary.

        Returns:
            dict: A dictionary containing the properties of the square.
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

