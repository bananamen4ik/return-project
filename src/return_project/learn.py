class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


counter = Counter(3)

print(next(counter))  # 1
print(next(counter))  # 2

for number in counter:
    print(number)  # 3

def __iter__(self):
    return self  # self потому что возвращается сам экземпляр у которого реализовано внутри next и сохранены данные его

class Counter:
    def __init__(self, limit):
        self.count = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.limit:
            raise StopIteration

        count = self.count
        self.count += 1

        return count


counter = Counter(5)

for number in counter:
    print(number)

class NumberRange:
    def __init__(self, low, high):
        self.count = low
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.high:
            raise StopIteration

        count = self.count
        self.count += 1

        return count


numbers = NumberRange(3, 7)

for number in numbers:
    print(number)

counter = Counter(3)

for number in counter:
    print(number)

for number in counter:
    print(number)  # Ничего не выведется так как counter тот же самый итератор, внутри которого уже достигнут лимит в next и все последующие будут вызывать StopIteration