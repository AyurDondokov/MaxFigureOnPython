class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def cord(self):
        return self.__x, self.__y

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


class Figure:
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
        return vec_area(v1, v2)

    def __str__(self):
        return f"[{self._points[0]}; {self._points[1]}; {self._points[2]}]"


class Quadrilateral(Figure):
    def _update_area(self):
        a = len_between_points(self._points[0], self._points[1])
        b = len_between_points(self._points[1], self._points[2])
        c = len_between_points(self._points[2], self._points[3])
        d = len_between_points(self._points[3], self._points[0])
        p = (a + b + c + d) / 2
        return float(((p - a)*(p - b)*(p - c)*(p - d)) ** 0.5)

    def __str__(self):
        return f"[{self._points[0]}; {self._points[1]}; {self._points[2]}; {self._points[3]}]"


def vec_area(v1, v2):
    return abs((v1.x * v2.y) - (v2.x * v1.y)) / 2


def len_between_points(p1, p2):
    return ((p2.x - p1.x)*(p2.x - p1.x)+(p2.y - p1.y)*(p2.y - p1.y)) ** 0.5


def is_convex_quadrilateral(points):
    t1 = ((points[3].x - points[0].x) * (points[1].y - points[0].y)
          - (points[3].y - points[0].y) * (points[1].x - points[0].x))
    t2 = ((points[3].x - points[1].x) * (points[2].y - points[1].y)
          - (points[3].y - points[1].y) * (points[2].x - points[1].x))
    t3 = ((points[3].x - points[2].x) * (points[0].y - points[2].y)
          - (points[3].y - points[2].y) * (points[0].x - points[2].x))
    t4 = ((points[0].x - points[2].x) * (points[1].y - points[2].y)
          - (points[0].y - points[2].y) * (points[1].x - points[2].x))
    return t1 * t2 * t3 * t4 > 0


def points_open(file_name):
    s = open(file_name, "r", encoding="utf-8").readline()
    s = s.replace('[', '')
    s = s.replace(',', '')
    s = s.split(']')[:-1]

    points = []
    for i in s:
        x, y = i.split()
        points.append(Point(int(x), int(y)))

    return points


def find_triangles_from_points(points):
    triangles_array = []
    count_of_triangles = len(points)
    for i in range(0, count_of_triangles - 2):
        for j in range(i, count_of_triangles - 1):
            for k in range(j, count_of_triangles):
                triangle = Triangle((points[i], points[j], points[k]))
                if triangle.get_area != 0.0:
                    triangles_array.append(triangle)
    return triangles_array


def find_max_min_quadrilaterals(points):
    quadrilaterals = [None, None]
    max_area = 0
    min_area = 10000000
    count_of_points = len(points)
    for i in range(0, count_of_points):
        for j in range(0, count_of_points):
            for k in range(0, count_of_points):
                for h in range(0, count_of_points):
                    points = (points[i], points[j], points[k], points[h])
                    if is_convex_quadrilateral(points):
                        four = Quadrilateral(points)
                        if four.get_area != 0:
                            if max_area < four.get_area:
                                quadrilaterals[0] = four
                                max_area = four.get_area
                            if min_area > four.get_area:
                                quadrilaterals[1] = four
                                min_area = four.get_area
    return quadrilaterals


point1 = Point(0, 0)
point2 = Point(5, 0)
point3 = Point(0, 5)
point4 = Point(5, 5)

print(Quadrilateral((point1, point2, point4, point3)).get_area)

pts = points_open("plist.txt")
print(f"Count of points: {len(pts)}")

triangles = sorted(find_triangles_from_points(pts))
n = len(triangles)
print(f"Count of triangles: {n}")
print(f"The smallest triangle: {triangles[0].get_area}\n The biggest triangle: {triangles[n-1].get_area}")

f = find_max_min_quadrilaterals(pts)
print(f"The smallest quadrilateral: {f[0].get_area}\n The biggest quadrilateral: {f[1].get_area}")
