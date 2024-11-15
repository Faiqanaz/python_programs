print("\tPRACTICE QUESTION OF While Loop")
print(" Enter 1 for Area Of Circle\n Enter 2 for Odd/Even\n Enter 3 for Vowel\n Enter 4 for Calculator")
print(" Enter 5 for Marksheet\n Enter 6 for Discount Program\n Enter 7 for Table of 3")

choice=input("Press 'y' to continue: ").lower()
while choice=='y' or choice=='yes':
    no=int(input("Enter Number: "))
    
       #Area of Circle
    if no==1:
        print("AREA OF CIRCLE")
        Pi=float(input("Enter the value of Pi: "))
        r=float(input("Enter the value of Radius: "))
        print("Area Of Circle:", Pi * (r ** 2))

        # Even/Odd
    elif no==2:
        print("EVEN/ODD")
        num=int(input("Enter a number: "))
        if num % 2==0:
            print("The Number is Even")
        else:
            print("The Number is Odd")

        # Vowel
    elif no==3:
        print("VOWEL")
        character=input("Enter a Character: ").lower()
        if character in 'aeiou':
            print(character, "is a Vowel")
        else:
            print(character, "is a Consonant")

        # Calculator
    elif no==4:
        print("CALCULATOR")
        num1=float(input("Enter First Number: "))
        num2=float(input("Enter Second Number: "))
        print(f"The Addition of numbers is: {num1 + num2}")
        print(f"The Subtraction of numbers is: {num1 - num2}")
        print(f"The Multiplication of numbers is: {num1 * num2}")
        print(f"The Division of numbers is: {num1 / num2}")
        print(f"The Reminder of numbers is: {num1 % num2}")
        print(f"The Integer Division of numbers is: {num1 // num2}")
        print(f"The Exponentiation of numbers is: {num1 ** num2}")

        # Marksheet
    elif no==5:
        print("MARKSHEET")
        name=input("Enter student's name: ")
        subjects=int(input("Enter the number of subjects: "))
        total=0
        for i in range(subjects):
            mark=float(input(f"Enter marks for subject {i + 1}: "))
            total+=mark
        percentage=(total / (subjects * 100)) * 100
        print(f"\nStudent Name: {name}")
        print(f"Total Marks: {total}")
        print(f"Percentage: {percentage:.2f}")
        if percentage>=90:
            grade='A+'
        elif percentage>=80:
            grade='A'
        elif percentage>=70:
            grade='B'
        elif percentage>=60:
            grade='C'
        elif percentage>=50:
            grade='D'
        else:
            grade='F'
        print(f"Grade: {grade}")

        # Discount Program
    elif no==6:
        print("DISCOUNT PROGRAM")
        total=0
        for i in range(5):
            price=float(input(f"Enter Price of item {i + 1}: "))
            total+=price
        print(f"Total cost: {total}")
        if total>=25000:
            discount=total * 0.25
        elif total>=10000:
            discount=total * 0.10
        else:
            discount=0
        amount_to_pay=total - discount
        print(f"Discount: {discount}")
        print(f"Amount to Pay: {amount_to_pay}")

        # Table of 3
    elif no==7:
        print("TABLE OF 3")
        for i in range(1, 11):
            print(f"3 * {i} = {3 * i}")

    else:
        print("Input is invalid")


    choice=input("Press 'y/yes' to continue: ").lower()