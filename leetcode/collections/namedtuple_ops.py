import collections


def main():
    # Creat a tuple named Point
    Point = collections.namedtuple('Point', "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    
    print(p1, p2)
    print(p1.y, p2.x)
    
    p1 = p1._replace(x=50)
    
    print(p1)

if __name__ == '__main__':
    main()