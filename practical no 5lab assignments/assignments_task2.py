prices = tuple(map(float, input("Enter price: ").split()))

if len(prices) > 0:
    print("\nTask (a) Total number of items sold:")
    print(len(prices))

    print("\nTask (b) Price of cheapest item sold:")
    print(min(prices))

    print("\nTask (c) Price of costliest item sold:")
    print(max(prices))

    print("\nTask (d) Price list in ascending order:")
    print(tuple(sorted(prices)))

    print("\nTask (e) Number of costliest items sold:")
    costliest = max(prices)
    print(prices.count(costliest))
else:
    print("No prices entered")