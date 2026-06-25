#Write a function that calculates the sum of all numbers from 1 to n using a loop.
def sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    print("Sum =",sum)
num=int(input("Enter a number:"))
sum(num)