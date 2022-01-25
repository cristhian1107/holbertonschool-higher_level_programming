#!/usr/bin/python3
"""Define an objects.
"""


class Rectangle:
    """Class Rectangle empty.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method - Initialize.

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Method - Draw the rectangle

        Returns:
            String content draw the rectangle (#)
        """
        drawn = ""
        if self.height != 0 and self.width != 0:
            for i in range(self.height):
                drawn += (str(self.print_symbol) * self.width) + "\n"
        return (drawn[:-1])

    def __repr__(self):
        """ Method - String represantion the rectangle

        Returns:
            String represantion the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """ Method - Deleted rectangle

        Returns:
            String 'Bye rectangle...'
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """ Method - Calculate area.

        Returns:
            Rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Method - Calculate perimeter

        Returns:
            Rectangle perimeter
        """
        if self.height == 0 or self.width == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    @property
    def width(self):
        """ Get - instance attribute width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set - instance attribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Get - instance attribute heigth
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set - instance attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
