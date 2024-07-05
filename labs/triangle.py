"""
3.4.10   LAB   Triangle
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class.
Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is what we want:

the constructor accepts three arguments – all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter
of the triangle described by the three points; the perimeter is the sum of all the lengths
of the legs (we mention this for the record, although we are sure that you know it perfectly yourself.)
Complete the template we've provided in the editor. Run your code and check whether
the evaluated perimeter is the same as ours.

Below you can copy the Point class code we used in the previous lab:

Expected: 3.414213562373095
"""

from math import pow, sqrt


class Point:
    """
    _summary_

    _extended_summary_
    """

    def __init__(self, x=0, y=0) -> None:
        self.__x = x
        self.__y = y

    def getx(self):
        """
        Returns:
            It will return the x coordinate of the current point
        """
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        """
        Args:
            x (int/float): x_coordinates
            y (int/float): y_coordinates

        Returns:
            float: returns the result using the euclidean formula
        """
        return sqrt(
            (pow((x - self.getx()), 2) + (pow((y - self.gety()), 2))))

    def distance_from_point(self, point):
        """
        Args:
            point: point object that contains getx and gety methods

        Returns:
            float: returns the result using the euclidean formula
        """
        # Euclidean distance formula
        # d = √((x₂ - x₁)² + (y₂ - y₁)²)
        point_x = point.getx()
        point_y = point.gety()
        return sqrt(
            (pow((point_x - self.getx()), 2) + (pow((point_y - self.gety()), 2))))


class Triangle:
    """
    A class to represent a triangle defined by three points.

    Attributes:
        __vertice_1 (float): The distance between the first and second vertices.
        __vertice_2 (float): The distance between the second and third vertices.
        __vertice_3 (float): The distance between the third and first vertices.

    Methods:
        perimeter(): Calculates the perimeter of the triangle.
    """

    def __init__(self, vertice1, vertice2, vertice3):
        """
        Constructs all the necessary attributes for the triangle object.

        Parameters:
            vertice1 (Point): The first vertex of the triangle.
            vertice2 (Point): The second vertex of the triangle.
            vertice3 (Point): The third vertex of the triangle.
        """
        # Calculate the distances between the vertices
        self.__vertice_1 = sqrt(pow(vertice2.getx() - vertice1.getx(), 2) + pow(vertice2.gety() - vertice1.gety(), 2))
        self.__vertice_2 = sqrt(pow(vertice3.getx() - vertice2.getx(), 2) + pow(vertice3.gety() - vertice2.gety(), 2))
        self.__vertice_3 = sqrt(pow(vertice1.getx() - vertice3.getx(), 2) + pow(vertice1.gety() - vertice3.gety(), 2))
        
    def perimeter(self):
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle.
        """
        return self.__vertice_1 + self.__vertice_2 + self.__vertice_3


# Example usage
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
# Output: 3.414213562373095
# Output: 3.414213562373095