import json

name = "bfo_hiprgen_small_dataset"

# Open and read the JSON file
with open(name+".json", 'r') as f:
    data = json.load(f)
#for i in range(len(data)):
#    print(i, data[i]["name"])
# Select the 1st, 4th, 5th, and 9th items from the list
selected_items = [data[1], data[4], data[5], data[12]]
for i in range(len(selected_items)):
    print(i, selected_items[i]["name"])
# Save the selected items to a new JSON file
with open(name+"_test.json", 'w') as f:
    json.dump(selected_items, f, indent=4)

print("Data has been saved to new test json")
