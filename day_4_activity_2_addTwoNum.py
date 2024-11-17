def addtwo():
    n1 = int(input("First Number : "))
    n2 = int(input("Second Number : "))


    print(n1 + n2)
    promp = input ("Do you want to try again? y/n : ")

    if promp == "y":
        return addtwo()
    else:
        print("Thank you!")
        exit

addtwo()