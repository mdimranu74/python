class multi():
    def SubfieldInAI():
        AI=["machine learning","neural networs","vision","robotics","speech processing","natural language processing"]
        print("Sub-fields in AI are:")
        for Subfields in AI:
            print(Subfields)
    def oddeven():
        number=int(input("enter the number:"))    
        if number%2 == 1 :
            print(number,"is odd number")
        else:
            print(number,"is even number")
    def MarriageElegibility():
        gender=input("Enter the gender:")
        age=int(input("Enter the age:"))
        if ((gender=="Male")&(age>=21)):
            print("eligible")
        elif ((gender=="Female")&(age>=18)):
            print("eligible")
        else:
            print("Not eligible")
    def percentage():
        sub1=int(input("subject1="))
        sub2=int(input("subject2="))
        sub3=int(input("subject3="))
        sub4=int(input("subject4="))
        sub5=int(input("subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total=", Total)
        per=(Total/5)
        print("Percentage :",per)
    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        print("Area Formula: (Height*Breadth)/2")
        A=(H*B)/2
        print("Area of triangle:", A)
        H1=int(input("Height1:"))
        H2=int(input("Height2:"))
        B1=int(input("Breadth1:"))
        print("perimeter Formula: height1+Height2+Breadth")
        P=H1+H2+B1
        print("Perimeter of triangle:", P)