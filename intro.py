name = "Joey"
hobby = "skateboarding"
job = "Developer"

print("My name is", name, "and I enjoy", hobby, "!"  )

cities = ["Nashville", "Murfreesboro", "Tullahoma"]

print(cities[2])

cities.append("Estill Springs")
cities.append("Lewisburg")
cities.append("Lexington")


print(cities)

expense = {
    "amount": 6.20,
    "category": "food",
    "note": "Bb"
}

print(expense["amount"])

if expense["amount"] > 10:
    print("Big Expense")
else:
    print("Small Expense")

for i in range(5):
    print("Looping...")

try:
    number = int("abc")
except ValueError as err:
    print("Conversion failed:", err)

print(f"My name is {name} and I am a {job}")

while True:
    cmd = input("Enter command: ")
    if cmd == "exit":
        break



