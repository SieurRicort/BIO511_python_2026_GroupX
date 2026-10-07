mylist = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
type(mylist)
print(mylist)
print(mylist[0])

items = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

#to loop through the list and print each item
for item in items:
    print(item) 

#to to loop through the list and print each item with its index instead of just the item
for index, item in enumerate(items, start=1):
    print(index)

#stop the loop after 5 items with if loop
for index, item in enumerate(items, start=1):
    if index <= 5:
        print(f"Item {index} is in the first 5 items.")



# While loops

sequence = 'GATTACAGAACTGATAC'









