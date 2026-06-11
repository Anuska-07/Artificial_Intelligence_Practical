#Write a program to check if a person is eligible to vote. Also check if they are a senior citizen (age >= 60).
age=int(input("Enter your age:"))
if age>18:
    print("You are eligible to vote.")
    if age>=60:
        print("Senior Citizen")
else:
    print("You are not eligible to vote.")