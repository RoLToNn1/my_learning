# Перевірте скільки голоснх букв в імені персонажа
name = "Harry Potter"
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0

for letter in name.lower():
    if letter in vowels:
        vowel_count += 1

print(f"Кількість голосних букв в імені Harry Potter = {vowel_count}")
