#Write a Python program which accepts the radius of a circle from the user and compute the area. (area of circle = PI * r2)

#class is used to calculate the Area of circle
class AreaOfCircle:
    def __init__(self):
        self.radius=float(input('Enter the radius of circle : '))

    def area(self):
        self.areaOfCircle=(22/7)*(self.radius**2)
        print('Area of Circle = ',self.areaOfCircle)

a= AreaOfCircle()
a.area()
