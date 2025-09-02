while True:
    rows = int(input("Enter row: "))
    cols = int(input("Enter col: "))
    search = int(input("Search: "))

    if rows <= 0 or cols <= 0:
        break

    i = 1
    while i <= rows:
        j = 1
        while j <= cols:
            product = i * j
            if product == search:
                print(f"[{product}]", end=" ")
            else:
                print(product, end="  ")
            j += 1
        print()
        i += 1