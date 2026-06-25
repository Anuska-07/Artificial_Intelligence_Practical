#Task 2: Implement a Model-Based Agent that maintains internal memory of the world state.

#Agent's internal memory
world_model={"A":"Clean","B":"Clean"}

def model_based_agent(location,status):
    #Update the agent's memory
    world_model[location]=status

    #Condition-Action Rules using memory
    if world_model["A"]=="Dirty":
        return "Go to A and Suck"
    elif world_model["B"]=="Dirty":
        return "Go to B and Suck"
    else:
        return "Do nothing, all are clean"
    
print("-----Model Based Agent-----")
print("Program by: Anuska Pradhan")
print("Roll no.: 7")

print("\nInitially, the state model contains:",world_model)
percepts=[("A","Dirty"),("A","Clean"),("B","Dirty"),("B","Clean")]
for percept in percepts:
    location,status=percept
    print("\nThe percept sequence is",(location,status))
    action=model_based_agent(location,status)
    print("Action:",action)
    print("The state model contains:",world_model)