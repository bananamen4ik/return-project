users = ["Armen", "John", "Alex"]

for index, name in enumerate(users, start=1):
    print(f"{index}. {name}")

names = ["Armen", "John", "Alex"]
ages = [27, 30, 25]

print(list(zip(names, ages)))

names = ["Armen", "John", "Alex"]
ages = [27, 30]

print(list(zip(names, ages)))

# Будет [("Armen", 27), ("John", 30)] так как zip останавливается на самом коротком объекте

numbers = [10, 20, -5, 30, 40]

print(any([number < 0 for number in numbers]))

numbers = [10, 20, 5, 30, 40]

print(all(number > 0 for number in numbers))

numbers = [10, 20, -5, 30, 40]

print(all(number > 0 for number in numbers))

users = [
    {"name": "Armen", "age": 27},
    {"name": "John", "age": 30},
    {"name": "Alex", "age": 25},
]

print(sorted(users, key=lambda user: user["age"]))
print(sorted(users, key=lambda user: user["age"], reverse=True))

numbers = [1, 2, 3, 4, 5]

print(list(reversed(numbers)))

users = [
    {"name": "Armen", "age": 27},
    {"name": "John", "age": 17},
    {"name": "Alex", "age": 25},
    {"name": "Maria", "age": 16},
]

print(any(user["age"] < 18 for user in users))
print(all(user["age"] >= 18 for user in users))
print(sorted(users, key=lambda user: user["age"]))
for index, user in enumerate(users):
    print(f"{index}. {user['name']}")
