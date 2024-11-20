#Practice

dict1 = {}
dict1["Madni"] = "Korejo"
dict1.update({"Class": "Software", "Batch": "2K21"})
print(dict1)

for key,value in dict1.items():
    print(f"{key} : {value}")

print([(key,value) for key,value in dict1.items()])
