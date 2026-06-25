#Write a program to count the number of vowels in a string.
text=input("Enter a string:")
count=0
vowels="aeiouAEIOU"
for char in text:
    if char in vowels:
        count+=1
print(f"The text has {count} no. of vowels")