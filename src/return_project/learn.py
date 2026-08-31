def generate_numbers():
    count = 1
    limit = 5

    while count <= limit:
        yield count
        count += 1


gen = generate_numbers()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def countdown(n):
    count = n

    while count > 0:
        yield count
        count -= 1


for number in countdown(5):
    print(number)

def squares(numbers):
    for number in numbers:
        yield number ** 2


for number in squares([1, 2, 3, 4]):
    print(number)

def counter():
    count = 0

    while True:
        yield count
        count += 1


gen = counter()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

numbers = (number ** 2 for number in range(1, 11) if number % 2 == 0)
print(type(numbers))

for number in numbers:
    print(number)

def test():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")

# При присвоении gen = test() будет создан объект генератора и выполнен print("A")
# Первый вызов next(gen) = вернет 10. Следующий вызов print("B") и вернет 20, следующий
# print("C") и StopIteration исключение

generator = test()

print("X")
print(next(generator))
print("Y")
print(next(generator))
print("Z")

# При присвоении generator = test() будет создан объект генератора и выполнен print("A")
# затем print("X"), далее print("A") и yield 10, далее print("Y"), далее print("B") и yield 20,
# далее print("Z")

def counter():
    value = 0

    while value < 3:
        yield value
        value += 1


generator = counter()

print(next(generator))  # 0
print(next(generator))  # 1
print(next(generator))  # 2

# И главное: почему value не сбрасывается в 0 при каждом next()? Потому что работаем внутри того же объекта generator
# у которого при создании создалась и помнится переменная value, yield не завершает функцию

numbers = [x * 2 for x in range(1_000_000)]
numbers = (x * 2 for x in range(1_000_000))

# Разница между ними в том что первый это list comprehension сразу создает список из миллиона элементов
# второй это генератор, который создает только объект генератора и ждем вызова next, чтобы выдать следующий элемент
# Что создаётся сразу? список
# Где хранятся вычисленные значения? Внутри итератора
# Что происходит при next() во втором варианте? Перебор элементов следующих
# 1. Почему генератор может быть выгоднее по памяти? Потому что в память не загружаются все данные, а выдаются лениво по мере вызова next

def read_numbers(numbers):
    return (number for number in numbers if number > 10)


numbers = [5, 15, 3, 20, 8, 30]

for number in read_numbers(numbers):
    print(number)
