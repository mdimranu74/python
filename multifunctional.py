class multiform():
     def subfields():
        AI=["machine learning","neural networs","vision","robotics","speech processing","natural language processing"]
        Subfield=input("Sub-field in AI are:")
        for subfields in AI:
            print(subfields)
     def oddeven():
        number=int(input("enter the number:"))    
        if number%2 == 1 :
            print(number,"is odd number")
            message= "odd number"
        else:
            print(number,"is even number")
            message= "even number"
     def eligibilityformarriage():
        gender=input("your gender:")
        age=int(input("your age:"))
        if (age>21):
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
        P=(Total/500)*100
        print("percentage:", P)
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