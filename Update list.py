hw_list = []
hw_list.append(["Math", 101, "Incomplete"])
hw_list.append(["French", 102, "Incomplete"])
print("Before: ", hw_list)

# Change French to "Complete"
assignment = "French"
for i in range(len(hw_list)):
    if hw_list[i][0] == assignment:
        hw_list[i][2] = "Complete"
print("After: ", hw_list)

