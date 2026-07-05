# Shopping List Builder.

shopping_items = []


while True:
    item_to_add = input("Add item to the shopping list (write done to quit): ")
    if item_to_add.lower() == 'done': break
    shopping_items.append(item_to_add)    
    

for item in shopping_items:
    print(item)