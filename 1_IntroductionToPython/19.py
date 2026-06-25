#Write a function that takes a number and returns whether it's even or odd.
def checker(num):
    if num%2==0:
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number.")
num=int(input("Enter a number: "))
checker(num)
