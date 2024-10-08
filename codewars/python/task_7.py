# Гравець 1 кидає кубикб а після цього Гравець 2 кидає кубик:
# У кубику є 1 2 3 4 5 6. Виграє той у кого більше випало.


import random


users_input = input("Ви готові?\n")


user_1 = random.randint(1, 6)
print(f"Гравецю 1 випало {user_1}")
user_2 = random.randint(1, 6)
print(f"Гравецю 2 випало {user_2}")


if user_1 > user_2:
    print("Гравець 1 виграв")
elif user_1 < user_2:
    print("Гравець 2 виграв")
else:
    print("Нічия")
