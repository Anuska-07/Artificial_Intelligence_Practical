#Task 1: Implement a Simple Reflex Agent using condition-action rules.
def simple_reflex_agent(location,status):
    #location: A or B / status: Dirty or Clean
    if status=="Dirty":
        return "Suck"
    elif location=="A":
        return "Move to B"
    elif location=="B":
        return "Move to A"
    else:
        return "No Operation"

print("-----Simple Reflex Agent-----")
print("Program by: Anuska Pradhan")
print("Roll no: 7")

percepts=[("A","Dirty"),("A","Clean"),("B","Dirty"),("B","Clean")]
for percept in percepts:
    location,status=percept
    print("\nThe percept sequence is",(location,status))
    action=simple_reflex_agent(location,status)
    print("Action:",action)