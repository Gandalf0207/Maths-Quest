EPS = 1E-9

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, p):
        return self.x < p.x - EPS or (abs(self.x - p.x) < EPS and self.y < p.y - EPS)

class Line:
    def __init__(self, p, q):
        self.a = p.y - q.y
        self.b = q.x - p.x
        self.c = -self.a * p.x - self.b * p.y
        self.norm()

    def norm(self):
        z = (self.a ** 2 + self.b ** 2) ** 0.5
        if abs(z) > EPS:
            self.a /= z
            self.b /= z
            self.c /= z

    def dist(self, p):
        return self.a * p.x + self.b * p.y + self.c

def det(a, b, c, d):
    return a * d - b * c

def betw(l, r, x):
    return min(l, r) <= x + EPS and x <= max(l, r) + EPS

def intersect_1d(a, b, c, d):
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    return max(a, c) <= min(b, d) + EPS

def intersect(a, b, c, d):
    if not intersect_1d(a.x, b.x, c.x, d.x) or not intersect_1d(a.y, b.y, c.y, d.y):
        return None  # Pas d'intersection

    m = Line(a, b)
    n = Line(c, d)
    zn = det(m.a, m.b, n.a, n.b)

    if abs(zn) < EPS:
        if abs(m.dist(c)) > EPS or abs(n.dist(a)) > EPS:
            return None  # Pas d'intersection
        return a if b < a else b  # Segments identiques, retourne un des points

    left = Point(-det(m.c, m.b, n.c, n.b) / zn, -det(m.a, m.c, n.a, n.c) / zn)
    if betw(a.x, b.x, left.x) and betw(a.y, b.y, left.y) and betw(c.x, d.x, left.x) and betw(c.y, d.y, left.y):
        return left  # Intersection des segments
    return None  # Pas d'intersection

# Coordonnées des points A, B, C et D
A = Point(13, -9)
B = Point(-41, 25)
C = Point(-2, -26)
D = Point(43, -45)

# Trouve le point d'intersection
intersection = intersect(A, B, C, D)

if intersection:
    print(f"Le point d'intersection est ({intersection.x}, {intersection.y})")
else:
    print("Pas d'intersection entre les segments.")
