items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items : 
    if item in items : 
        print("Duplicate Items ", item)
        break
    unique_item.add(item)
