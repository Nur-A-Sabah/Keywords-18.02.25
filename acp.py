def due(b,g):
    return g-b

bill = int(input("Enter bill amount: "))
given = int(input("Enter given amount: "))

dueAmount = due(bill, given)

print(f"Due Amount : {dueAmount}")