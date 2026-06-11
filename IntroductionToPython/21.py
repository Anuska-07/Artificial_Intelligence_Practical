#Write a function that prints the multiplication table of any number.
def multiplication(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
num=int(input("Enter a number:"))
multiplication(num)