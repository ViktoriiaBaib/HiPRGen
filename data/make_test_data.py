import json

fname = "bfo_hiprgen_dataset"

# Open and read the JSON file
with open(fname+".json", 'r') as f:
    data = json.load(f)
#for i in range(len(data)):
#    print(i, data[i]["name"])
# Select the 1st, 4th, 5th, and 9th items from the list
#selected_items = [data[1], data[4], data[5], data[12]]
#for i in range(len(selected_items)):
#    print(i, selected_items[i]["name"])
#Select by name
names = ["2809_graph773_cn6_pentagonal_pyramidal_0_nunpairedes_0_charge_0", 
"0210_graph620_cn6_trigonal_prismatic_0_nunpairedes_0_charge_0", 
"2809_graph397_cn6_pentagonal_pyramidal_0_nunpairedes_0_charge_0",
"2809_graph476_cn5_trigonal_bipyramidal_0_nunpairedes_0_charge_0",
"ind95_graph610_cn5_trigonal_bipyramidal_0_nunpairedes_0_charge_0",
"2609_graph207_cn6_trigonal_prismatic_0_nunpairedes_0_charge_0",
"ind44_graph207_cn6_trigonal_prismatic_0_nunpairedes_0_charge_0",
"_graph70_", "_graph82_", "_graph69_", "_graph306_",
"2809_graph149_cn6_hexagonal_planar_0_nunpairedes_0_charge_0",
"_graph1_", "_graph32_",
"ind71_graph356_cn6_trigonal_prismatic_4_nunpairedes_0_charge_0",
"_graph218_", "_graph463_",
"no3_ion_opt", "hno3_opt", "moe_ion_opt", "moe_opt"]
# Save the selected items to a new JSON file
selected_items = []
for i,doc in enumerate(data):
    for name in names:
        if name in doc["name"]:
            selected_items.append(doc)
            print(i, doc["name"])
with open(fname+"_test.json", 'w') as f:
    json.dump(selected_items, f, indent=4)

print("Data has been saved to new test json")
