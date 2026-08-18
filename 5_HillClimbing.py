# Hill Climbing Search

# Step 1: Define the landscape
landscape = [2, 5, 8, 12, 10, 15, 11, 13, 9, 14]

# Step 2: Display the landscape
print("-" * 50)
print("HILL CLIMBING SEARCH (DYNAMIC)")
print("-" * 50)
print()

print("Index: ", end="")
for i in range(len(landscape)):
    print(f"{i:4}", end="")
print()

print("Value: ", end="")
for val in landscape:
    print(f"{val:4}", end="")
print("\n")


# Step 3: Simple Hill Climbing Function
def simple_hill_climb(start):
    current = start

    print(f"Start at Index {current}, Value {landscape[current]}")
    print("Climbing...")

    while True:
        moved = False

        # Check left
        if current > 0 and landscape[current - 1] > landscape[current]:
            current = current - 1
            moved = True
            print(f"  Move left to {current}, Value {landscape[current]}")

        # Check right
        elif current < len(landscape) - 1 and landscape[current + 1] > landscape[current]:
            current = current + 1
            moved = True
            print(f"  Move right to {current}, Value {landscape[current]}")

        # If no move, peak reached
        if not moved:
            print()
            print(f"Peak reached at Index {current}, Value {landscape[current]}")
            break

    if landscape[current] == max(landscape):
        print("✓ GLOBAL MAXIMUM FOUND!\n")
    else:
        print("⚠️ LOCAL MAXIMUM (not the highest)\n")

    return current


# Step 4: Test from multiple starting positions
start_positions = [5, 2, 7, 0]

for start in start_positions:
    print("-" * 40)
    simple_hill_climb(start)