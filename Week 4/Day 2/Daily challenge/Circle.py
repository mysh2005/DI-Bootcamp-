import math

class Circle:
    def __init__(self, radius=0, diameter=0):
        if radius > 0:
            self.radius = radius
        elif diameter > 0:
            self.radius = diameter / 2
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    #Print the attributes of the circle
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area})"

    #Add two circles together
    def __add__(self, other):
            return Circle(radius=self.radius + other.radius)
    
    #Compare two circles to see which is bigger
    def __lt__(self, other):
            return self.radius < other.radius
    
    #Compare two circles and see if there are equal
    def __eq__(self, other):
            return self.radius == other.radius
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"

circle1 = Circle(radius=5)
circle2 = Circle(diameter=15)
print(circle1)  
print(circle2)  

circle3 = circle1 + circle2
print(circle3)  

print(circle1 < circle2) 
print(circle1 == circle2)  

#Put the circles in a list and sort them
circles = [Circle(radius=10), Circle(radius=1), Circle(radius=6)]
circles.sort()
print(circles) 
