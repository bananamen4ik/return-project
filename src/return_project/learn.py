def count_to_three():
    yield 1
    yield 2
    yield 3


counter = count_to_three()
print(next(counter))
print(next(counter))
print(next(counter))


def count_to(limit):
    count = 1

    while count <= limit:
        yield count
        count += 1


counter = count_to(3)
print(next(counter))
print(next(counter))
print(next(counter))

counter = count_to(3)
for i in counter:
    print(i)

# Генератор отличается от моего итератора тем, что здесь используются функции и конструкция yield, и даже не нужно самому вызывать StopIteration, при завершении next сам понимает
# Да и насколько я знаю по сути генераторы нужны для оптимизации программы, чтобы не высчитывать все сразу, а по мере необходимости, когда как итераторы идут по конкретной готовой уже коллекции зачастую
