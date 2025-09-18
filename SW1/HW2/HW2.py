
mydict = {}

size = int(input('Matrix Size: ')) #matrix size

for i in range(size):

    value = input(f'Shopping Items {i+1}: ')   #add
    mydict[i] = value

print("You have", len(mydict), "items in the cart")

while True:
    choice = input("[C]hange  [R]emove  [D]isplay  [S]earch  [*]Exit: ").lower()

    if choice == "d":   # display
        print("Key   Value")
        for k, v in mydict.items():
            print(k, "   ", v)

    elif choice == "s":   # search
        item = input("Enter key or value to search: ")
        if item.isdigit():
            key = int(item)
            if key in mydict:
                print("Found:", mydict[key])
            else:
                print("Not in the cart")
        else:
            if item in mydict.values():
                print("Found:", item)
            else:
                print("Not in the cart")

    elif choice == "r":   # remove
        key = input("Enter key to remove: ")
        if key.isdigit():
            key = int(key)
            if key in mydict:
                print("Removed:", mydict[key])
                mydict.pop(key)
            else:
                print("Key not found")
        else:
            print("Key not found")

    elif choice == "c":   # change
        key = input("Enter key to change: ")
        if key.isdigit():
            key = int(key)
            if key in mydict:
                print("Current value:", mydict[key])
                mydict[key] = input("Enter new value: ")
            else:
                print("Key not found")
        else:
            print("Key not found")

    elif choice == "*":   # exit
        print("Bye")
        break

    else:
        print("Invalid choice")
