import random
import math

#Question 5: Circle Area Comparison with Validation

def circle_area_coverage(radius_of_circle1, radius_of_circle2): #intialized function taking 2 parameters of 2 different circle radii
    if radius_of_circle1 and radius_of_circle2 >=0: #checks if the radius of the circles is positive
        area_of_circle1 = (radius_of_circle1 ** 2) * math.pi #calculates area of the two circles
        area_of_circle2 = (radius_of_circle2 ** 2) * math.pi
        if area_of_circle1 > area_of_circle2: #checks which circle has the larger area
            percentage_of_smaller_circle_area_coverage = area_of_circle2/  area_of_circle2 #finds the percentage of the smaller circle in the bigger circle
            return percentage_of_smaller_circle_area_coverage #returns the area percentage the smaller circle takes in the bigger one
        else: # executed if circle 2 is larger than circle 1
            percentage_of_smaller_circle_area_coverage = area_of_circle1 / area_of_circle2
            return percentage_of_smaller_circle_area_coverage
    return None #returns nothing if radius is negative

areaCoverage = circle_area_coverage(random.randint(1, 10), random.randint(1, 10))

if areaCoverage is not None:
    print(f"The percentage of the larger circle’s area that can be covered by the smaller circle is {areaCoverage}")
else:
    print("The Radius of the Circle Cannot Be Negative")