print("\tPRACTICE QUESTION OF IF AND IF-ELSE LADDER")
print(" Enter 1 for Area Of Circle\n Enter 2 for Odd/Even\n Enter 3 for Vowel\n Enter 4 for Calculator\n Enter 5 for Marksheet")
choice=eval(input("Enter choice:"))
   # area of circle
if choice==1:
    print("AREA OF CIRCLE")
    Pi=eval(input("Enter the value of Pi: "))
    r=eval(input("Enter the value of Radius: "))
    print("Area Of Circle:", Pi*(r**2))
   # Even/Odd
elif choice==2:
    print("EVEN/ODD")
    num=eval(input("Enter a number:"))
    if num%2==0:
        print("The Number is Even")
    else:
        print("The Number is Odd")
    # Vowel
elif choice==3:
    print("VOWEL")
    character=input("Enter a Character:").lower()
    if character=='a'or character=='e'or character=='i'or character=='o'or character=='u':
        print(character,"is a Vowel")
    else:
        print(character,"is a Consonant")
    # Calculator
elif choice==4:
    print("CALCULATOR")
    no1=eval(input("Enter First Number:"))
    no2=eval(input("Enter Second Number:"))
    print("The Addition of no1 and no2 is equal to ",no1 + no2)
    print("The Subtraction of no1 and no2 is equal to ",no1 - no2)
    print("The Multiplication of no1 and no2 is equal to ",no1 * no2)
    print("The Division of no1 and no2 is equal to ",no1 / no2)
    print("The Reminder of no1 and no2 is equal to ",no1 % no2)
    print("The Integer Division of no1 and no2 is equal to ",no1 // no2)
    print("The Exponentiation of no1 and no2 is equal to ",no1 ** no2)
    # Marksheet
elif choice==5:
    print("MARKSHEET")
    name=input("\nEnter student's name:")
    subjects=int(input("Enter the number of subjects:"))
    tot=0
    for nos in range(subjects):
        mark=float(input("Enter marks for subjects:"))
        tot+=mark
    per=(tot/(subjects*100))*100
    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {tot}")
    print(f"Percentage: {per:.2f}")
    if per>=90:
        grade='A+'
    elif per>=80:
        grade='A'
    elif per>=70:
        grade='B'
    elif per>=60:
        grade='C'
    elif per>=50:
        grade='D'
    else:
        grade='F'
        
    print(f"Grade:{grade}")
    
else:
    print("Input is invalid")

    