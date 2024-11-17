#Object oriented Grading System 
fname = input("Name : ")
lname = input("Sur : ")
math = input("Math Grade : ")
science = input("Science Grade : ")
english = input("English Grade : ")


class GradingSys():
    def __init__(self, fname, lname, math,science ,english ):
        #=====Varibles=====#

        #first name last name

        self.fname = str(fname)
        self.lname = str(lname)

        #grades
        self.math = float(math)
        self.science = float(science)
        self.english = int(english)

        self.status = ""

    def run(self):
        #calculate the grades
        print(f"Name : {self.fname} {self.lname}")
        self.calculate = self.math + self.english + self.science
        self.calculate /= 3

        #output of grades
        print(f"Math    : {self.math}")
        print(f"Science : {self.science}")
        print(f"English : {self.english}")
        
        #logic if nka pasa or bagsak sa isang sub

        if self.calculate > 74 and self.math < 75:
            print("Congratulations! you passed the semester. But you need to re-enroll Math")
        
        if self.calculate > 74 and self.science < 75:
            print("Congratulations! you passed the semester. But you need to re-enroll Science")

        if self.calculate > 74 and self.english < 75:
            print("Congratulations! you passed the semester. But you need to re-enroll English")

        elif self.calculate < 75:
            self.status = "Failed"

        else:
            self.status = "Passed"

        print(f"Final Grade : {round(self.calculate, 1)} | Status  : {self.status}")

#run
            #Name  #LastName  #Math Science English
GradingSys(fname , lname , math , science , english).run()