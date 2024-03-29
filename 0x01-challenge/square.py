#!/usr/bin/python3
# Fixed and updated by: ArtaxJay Olaoluwa

class Square:
    """
    Creates a class that computes the Swuare of two values.
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Declare class variables """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a str representation of the square class.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
