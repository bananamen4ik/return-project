# numbers = [1, 2, 3, 4, 5]


# print(list(map(lambda number: number * 10, numbers)))

# def square(number):
#     return number ** 2
#
#
# print(list(map(square, numbers)))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list(filter(lambda number: number % 2 == 0, numbers)))

# def is_adult(age):
#     return age >= 18
#
#
# ages = [12, 17, 18, 25, 15, 30]
#
# print(list(filter(is_adult, ages)))

# numbers = [1, 2, 3]
#
# result = map(lambda x: x * 10, numbers)
#
# print(next(result))  # 10
# print(next(result))  # 20
# print(list(result))  # [30]


# numbers = [1, 2, 3, 4, 5, 6]
#
# print(
#     list(
#         map(
#             lambda number: number * 10,
#             filter(lambda number: number % 2 == 0, numbers)
#         )
#     )
# )

numbers = [1, 2, 3, 4, 5, 6]

print(
    list(
        map(
            lambda number: number ** 2,
            filter(lambda number: number % 2 == 0, numbers)
        )
    )
)

print([
    number ** 2
    for number in numbers
    if number % 2 == 0
])  # Этот вариант более читабельный, так как менее громоздкий

# Разница между result = map(...) и result = list(map(...))
# В первом варианте возвращается итератор, по которому можно лениво идти
# Во втором варианте уже готовый список
# Лениво в первом случае проходят из-за того, что мы по мере необходимости
# идем по итератору и не вычисляем все сразу
