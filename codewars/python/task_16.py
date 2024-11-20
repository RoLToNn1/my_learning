# Створіть функцію, яка відповідає на питання «Ви граєте на банджо?».
# Якщо ваше ім'я починається з літери "R" або малої букви "r", ви граєте на банджо!
#
# Функція приймає назву як єдиний аргумент і повертає один із таких рядків:
#
# name + " plays banjo"
# name + " does not play banjo"
# Надані імена завжди є дійсними рядками.
name = input("Enter your name: ")
def playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo."
    else:
        return name + " doesn't play banjo."
result = playing_banjo(name)
print(result)
