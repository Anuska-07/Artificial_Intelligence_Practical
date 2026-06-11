#Write a function to reverse a string using a loop.
def reverse_string(text):
    reverse = ""
    for ch in text:
        reverse= ch+reverse
    return reverse
text=input("Enter a string: ")
print(reverse_string(text))