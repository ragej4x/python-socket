import math
# meron tayong 3 variable so angle a, b, c
# calculate the distance between angles
# evry angle we have spec deg each side
# if d nag match ung isang side then output nung whenever anong angle
#      a
#       ^
#     / \
#    /  \
#   /   \
# b/----\c
class Angle():
    def __init__(self):

        self.a = float(input("A : "))

        self.b = float(input("B : "))
        
        self.c = float(input("C : "))

        print("\n")

    def calculate(self):
        # calculate degree of an angle 

        A = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
        B = math.degrees(math.acos((self.c**2 + self.a**2 - self.b**2) / (2 * self.c * self.a)))
        C = math.degrees(math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)))

        #logic

        print("============================================")
        if A == B == C:
            print("Equilateral Triangle")
        elif A == B or B == C or C == A:
            print("Isosceles Triangle")
        else:
            print(" Scalene Triangle")

        print("============================================\n")

        print("Degree")
        print(f"A = {round(A, 2)}°")
        print(f"B = {round(B, 2)}°")
        print(f"C = {round(C, 2)}°")

Angle().calculate()