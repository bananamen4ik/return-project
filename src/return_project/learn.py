class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Armen", "John"])

print(len(team))


class User:
    def __init__(self, name, age):
        self.data = {
            "name": name,
            "age": age
        }

    def __getitem__(self, item):
        return self.data[item]


user = User("Armen", 27)
print(user["name"])
print(user["age"])


class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, member):
        return member in self.members


team = Team(["Armen", "John"])

print("Armen" in team)


class Team:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)


team = Team(["Armen", "John"])

for member in team:
    print(member)


class Counter:
    def __init__(self, limit):
        self.count = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.limit:
            raise StopIteration

        current = self.count
        self.count += 1

        return current


for count in Counter(5):
    print(count)


class Multiplier:
    def __init__(self, value):
        self.value = value

    def __call__(self, number):
        return self.value * number


double = Multiplier(2)

print(double(10))
print(double(5))


class DatabaseConnection:
    def __enter__(self):
        print("Connected")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Disconnected")


with DatabaseConnection():
    print("Working")

with DatabaseConnection():
    raise ValueError("Something went wrong")


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, user):
        return self.user_id == user.user_id


print(User(1) == User(1))
print(User(1) == User(2))

user1 = User(1)
user2 = User(1)

print(user1 is user2)

for x in obj:
    print(x)

# в obj ищется итератор и возвращается объект с итератором, далее в объекте-итераторе поочередно вызывается next и возвращается значение до исключения StopIteration
# iter(obj) - Вызывается __iter__
# next(iterator) - Вызывается __next__
# StopIteration - исключение, которое завершает итерации

# len(obj) - __len__
# obj["name"] - __getitem__
# "name" in obj - __contains__
# for x in obj: - __iter__, __next__
# obj() - __call__
# with obj: - __enter__, __exit__

# Разница между Iterable и Iterator и Generator в том, что:
# Iterable это объект по которому можно пройти итератором, поддерживает перебор, коллекции типа list, dict, set, tuple
# Iterator это сама реализация протокола в объекте для прохода по элементам объекта
# Generator это метод создания итератора через функцию с помощью yield

# Является ли каждый generator iterator'ом? Да
# Является ли каждый iterator generator'ом? Нет
