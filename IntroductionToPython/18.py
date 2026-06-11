#Write a program to check if a string is a palindrome (reads the same forwards and backwards).
text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse
if text == reverse:
    print("String is a palindrome")
else:
    print("String is not a palindrome")