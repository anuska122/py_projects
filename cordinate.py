# Coordinate data type

class Point:

    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))


class Line:
    def __init__(self,A,B,C):
        self.A= A
        self.B= B
        self.C= C
    
    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.A,self.B,self.C)
    
    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return " Point lies in the line"
        else:
            return "Point does not lies in the line"
    
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/ (line.A**2 + line.B**2)**0.5
    
    def intersect(line1,line2):
        a1,b1,c1 = line1.A, line1.B, line1.C
        a2,b2,c2 = line2.A,line2.B,line2.C

        determinant = a1*b2-a2*b1
        if determinant != 0:
            return "Line intersect"
        else:
        
            if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
                return "The lines are coincident (overlap entirely)."
            else:
                return "The lines are parallel an#d do not intersect."


l1 = Line(1,1,-2)
p1 = Point(1,1)
result = l1.shortest_distance(p1)

print(l1)
print(p1)
print(result)

l2 = Line(2, -1, 3)
intersection_result = Line.intersect(l1, l2)
print("Intersection Result:", intersection_result)

# p1 = Point(0,0)
# p2 = Point(10,10)
# result = p1.distance_from_origin()
# print(result)
