users = ["Armen", "John", "Alex"]

for index, name in enumerate(users, start=1):
    print(f"{index}. {name}")

names = ["Armen", "John", "Alex"]
ages = [27, 30, 25]

print({
    name: age
    for name, age in zip(names, ages)
})

ages = [15, 16, 17, 20]

print(any(map(lambda age: age >= 18, ages)))

ages = [20, 25, 30, 19]

print(all(map(lambda age: age >= 18, ages)))

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 10, numbers)))
# Тип до list generator хотел написать, затем проверил и type показывает map почему?

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: x % 2 == 0, numbers)))

users = [
    {"name": "Armen", "age": 27},
    {"name": "John", "age": 20},
    {"name": "Alex", "age": 35},
    {"name": "Maria", "age": 25},
]

print(sorted(users, key=lambda x: x["age"], reverse=True))

numbers = [3, 1, 2]

result = sorted(numbers)

print(result)  # [1, 2, 3]
print(numbers)  # [3, 1, 2]
# Отличие от numbers.sort(), что numbers.sort() изменяет сам список, а sorted новый возвращает отсортированный

names = ["Armen", "John", "Alex"]
scores = [95, 87, 91]

for index, user in enumerate(zip(names, scores), start=1):
    print(f"{index}. {user[0]} - {user[1]}")

a = [1, 2, 3]
b = [4, 5]
c = [6, 7]

from itertools import chain

print(list(chain(a, b, c)))

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))  # [2, 4, 6, 8]
print(list(result))  # [] так как result уже полностью весь пройден предыдущим вызовом

users = [
    {"name": "Armen", "age": 27, "active": True},
    {"name": "John", "age": 17, "active": True},
    {"name": "Alex", "age": 30, "active": False},
    {"name": "Maria", "age": 25, "active": True},
]

print([
    user["name"]
    for user in filter(lambda user: (user["age"] >= 18 and user["active"]), users)
])
