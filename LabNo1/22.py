#Create a function that converts marks to grades using if-elif-else.
def grades(marks):
    if marks>=90 and marks<=100:
        print("Grade: A")
    elif marks>=80 and marks<=89:
        print("Grade: B")
    elif marks>=70 and marks<=79:
        print("Grade: C")
    elif marks>=60 and marks<=69:
        print("Grade: D")
    elif marks<60:
        print("Grade: F")
    else:
        print("Invalid Marks!")
marks=int(input("Enter your marks:"))
grades(marks)