# Створіть функцію,
# яка приймає ціле число i повертає «Even» для парних чисел або «Odd» для непарних чисел.


def number_counter(list_for_count):
    even_number_counter = 0
    odd_number_counter = 0
    for item in list_for_count:
        if item / 2 == item // 2:
            even_number_counter += 1
        else:
            odd_number_counter += 1
    return odd_number_counter, even_number_counter


my_list = [
    7, 14, 9, 22, 1, 6,
    11, 16, 3, 8, 19, 12,
    5, 18, 13, 2, 21, 4, 17, 10
]

odd_count, even_count = number_counter(my_list)
print(f"Непарних чисел: {odd_count}, Парних чисел: {even_count}")




