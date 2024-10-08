#region Задача: Зірка з п'яти променів
# Напиши програму, яка використовує модуль turtle для малювання зірки з пяти променів.'
# Кожен промінь повинен мати довжину 150 одиниць.)
#
# Вимоги:
# Використати модуль turtle.
# Черепашка повинна намалювати п'ятикутну зірку.
# Довжина кожного проміння має бути 150 одиниць.
# Програма повинна завершитись автоматично після малювання.
# Підказка:
# Щоб намалювати зірку, черепашка повинна робити повороти під кутом 144 градуси після
# endregion


import turtle


my_turtle = turtle.Turtle()
screen = turtle.Screen()


my_turtle.left(36)
for _ in range(5):
    my_turtle.forward(150)
    my_turtle.left(144)


screen.mainloop()