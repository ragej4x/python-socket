#Object oriented Grading System 
fname = input("Name : ")
lname = input("Sur : ")
math = input("Math Grade : ")
science = input("Science Grade : ")
english = input("English Grade : ")


class GradingSys():
    def __init__(self, fname, lname, math,science ,english ):
        #=====Varibles=====#

        #First name Last name

        self.fname = str(fname)
        self.lname = str(lname)

        #Grades
        self.math = float(math)
        self.science = float(science)
        self.english = int(english)

        self.status = ""

    def run(self):
        #calculate the grades
        #calculate grade divide by how many subs increment by sub nalang po if mag dadagdag

        print(f"Name : {self.fname} {self.lname}")
        self.calculate = self.math + self.english + self.science
        self.calculate /= 3

        #output of grades
        print(f"Math    : {self.math}")
        print(f"Science : {self.science}")
        print(f"English : {self.english}")
        
        #check if passed

        if self.calculate > 74:
            self.status = "Passed"
        else:
            self.status = "Failed"

        print(f"Grade : {round(self.calculate, 1)} | Status  : {self.status}")

#run
            #Name  #LastName  #Math Science English
GradingSys(fname , lname , math , science , english).run()