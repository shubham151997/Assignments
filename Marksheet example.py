physics = int(input("Physics marks"))
Chemistry = int(input("Chemistry marks"))
Math = int(input("Math marks"))
Bio = int(input("Bio marks"))
Eng = int(input("Eng marks"))
Hindi = int(input("Hindi marks"))
Science = int(input("Science marks"))
PT = int(input("PT marks"))
Total_Marks = physics+Chemistry+Math+Bio+Eng+Hindi+Science+PT
Percentage = (Total_Marks*100)/800

#Total marks
print("Total Marks =", Total_Marks)

#Percentage
print("Percentage = ",(Percentage))
if physics>=35 and Chemistry>=35 and Math>=35 and Bio>=35 and Eng>=35 and Hindi>=35 and Science>= 35 and PT >=35:
    print("Pass")

    if Percentage >=90:
        print("Pass with Merit")
        
    elif Percentage >=75 and Percentage <= 89:
            print("Pass with distinction")

    elif Percentage >=60 and Percentage <= 74:
            print("Pass with First class")

    else:
        print("Pass with Second class")

else:
    print("Fail")
