categories = ["Food", "Bills", "Shopping", "General"]

for category in categories:
    print(category)

expense = {
   "category": "Bills",
    "amount": 41.00,
    "note": "gas"
}   

if expense["amount"] > 62 :
    print("Big Expense")
else:
    print("Small Expense")

userValue = input("Enter a number: ")

try:
   num = int(userValue)
   print(num)
except ValueError:
    print("That was not a number!")