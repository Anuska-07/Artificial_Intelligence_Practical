#Task 3: Test both agents with different percept sequences.

#-----Model Based Agent-----
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
    
#-----Simple Reflex Agent-----
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
    
#-----Test Percepts-----
percepts=[("A","Dirty"),("A","Clean"),("B","Dirty"),("B","Clean")]

#------Display Model Based Agent-----
print("="*70)
print("Model-Based Agent(with memory)")
print("="*70)
print(f"\n{'Percept':<15}" {'Action':<30} {'Memory After':<20}")
print("-" * 70)


world_model = {"A": "Clean", "B": "Clean"}
for location, status in percepts:
    action = model_based_agent(location, status)
    print(f"({location}, {status:<5})  {action:<30} {world_model}")


# ========== DISPLAY SIMPLE REFLEX AGENT ==========
print("\n" + "=" * 70)
print("SIMPLE REFLEX AGENT (No Memory)")
print("=" * 70)
print(f"\n{'Percept':<15} {'Action':<20}")
print("-" * 70)


for location, status in percepts:
    action = simple_reflex_agent(location, status)
    print(f"({location}, {status:<5})  {action}")


# ========== COMPARISON TABLE ==========
print("\n" + "=" * 70)
print("COMPARISON TABLE")
print("=" * 70)
print(f"\n{'Percept':<15} {'Model-Based':<25} {'Simple Reflex':<20}")
print("-" * 70)


world_model = {"A": "Clean", "B": "Clean"}
for location, status in percepts:
    world_model = {"A": "Clean", "B": "Clean"}
    mb_action = model_based_agent(location, status)
    sr_action = simple_reflex_agent(location, status)
    print(f"({location}, {status:<5})  {mb_action:<25} {sr_action}")
