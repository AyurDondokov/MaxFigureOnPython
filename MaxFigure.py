import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @property
    def cord(self):
        return (self.__x, self.__y)
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    def __eq__(self, b):
        return self.__x == b.__x and self.__y == b.__y
    def __ne__(self, b):
        return self.__x != b.__x or self.__y != b.__y
    def __str__(self):
        return f"({self.__x}; {self.__y})"

def VecS(v1, v2):
    return (abs( (v1.x * v2.y) - (v2.x * v1.y) ) / 2)

class Figure():
    def __init__(self, points):
        self._points = points
        self.__area = self._update_area()
    def _update_area(self):

        print("Figure::__update_area")
        pass

    @property
    def get_area(self):
        return self.__area
    def __lt__(self, b):
        return self.__area < b.__area
    def __le__(self, b):
        return self.__area <= b.__area
    def __eq__(self, b):
        return self.__area == b.__area
    def __ne__(self, b):
        return self.__area != b.__area
    def __ge__(self, b):
        return self.__area >= b.__area
    def __gt__(self, b):
        return self.__area > b.__area

class Triangle(Figure):
    def _update_area(self):
        v1 = Point(self._points[0].x - self._points[1].x,
                   self._points[0].y - self._points[1].y)
        v2 = Point(self._points[2].x - self._points[1].x,
                   self._points[2].y - self._points[1].y)
        return VecS(v1, v2)

    def __str__(self):
        return f"{self._points[0]}; {self._points[1]}; {self._points[2]}"

def points_open(fileName):
    s = open(fileName, "r", encoding="utf-8").readline()
    s = s.replace('[', '')
    s = s.replace(',', '')
    s = s.split(']')[:-1]

    pts = []
    for i in s:
        x, y = i.split()
        pts.append(Point(int(x), int(y)))

    return pts

def triangles_finder(pts):
    triangles = []
    n = len(pts)
    for i in range(0, n-2):
        for j in range(i, n-1):
            for k in range(j, n):
                tri = Triangle((pts[i], pts[j], pts[k]))
                if (pts[i] != pts[j] and pts[j] != pts[k]):
                    triangles.append(tri)
    return triangles


point1 = Point(0, 0)
point2 = Point(5, 0)
point3 = Point(0, 5)
t = Triangle( (point1, point2, point3) )

pts = points_open("plist.txt")
triangles = sorted(triangles_finder(pts))
n = len(triangles)
print(triangles[0], triangles[n-1])



