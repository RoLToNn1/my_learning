#region У мене є кіт і собака.
#
# Людські роки лише цілими числами

# Котячі роки

# 15котячих років за перший рік
# +9котячих років на другий рік
# +4котячих років для кожного наступного року

# Собачі роки

# 15років собаки за перший рік
# +9собачі роки на другий рік
#endregion +5собачих років для кожного наступного року

user_age = int(input("Put your age -->\n"))
cats_age = int(input("Puy cat's age -->\n"))
dogs_age = int(input("Put dog's age -->\n"))


if cats_age == 1:
    cats_age += 15
elif cats_age == 2:
    cats_age += 9
elif cats_age == 3:
    for _ in range(cats_age):
        cats_age += 4


if dogs_age == 1:
    dogs_age += 15
elif dogs_age == 2:
    dogs_age += 9
elif dogs_age == 3:
    for _ in range(dogs_age):
        dogs_age += 5

print(f"User age: {user_age} years old."
f" Your cat's age in people age: {cats_age}."
f" Your dogs age in people age: {dogs_age}")