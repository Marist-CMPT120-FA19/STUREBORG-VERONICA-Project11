#Veronica Stureborg
#Project 11

from math import *

class Sphere:

    def __init__(self, r):
        self.radius= r
        self.volume = 0
        self.area = 0
        #create sphere with given radius

    def getRadius (self):
        return self.radius
        #Returns the radius of the sphere.

    def surfaceArea(self):
        r= self.radius
        self.area = (4*pi*(r**2))
        return self.area
        #Returns the surface area of the sphere.

    def volume(self):
        r=self.radius
        self.volume = ((4/3)*pi*(r**3))
        return self.volume 
        #Returns the volume of the sphere.

def main():
    r=float(input("Enter a number for the radius: "))
    sphere= Sphere(r)

    volume= ((4/3)*pi*(r**3))
    area= (4*pi*(r**2))
    print("The volume of the sphere is: ", volume)
    print("The area of the sphere is: ", area)

if __name__ == '__main__':
    main()
