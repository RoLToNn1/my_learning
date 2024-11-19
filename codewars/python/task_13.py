# Дано list зробіть так щоб рядок повернувся у формі короткий+довгий+короткий,
# з коротшим рядком назовні та довшим усередині.
list = ["ironman", "halk", "doktor streng", "tor"]
longest = max(list, key=len)
shortest = min(list, key=len)
print(longest + ", " + shortest + ", " + longest)