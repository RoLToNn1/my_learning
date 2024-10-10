#region Напишіть функцію bmi, яка обчислює індекс маси тіла (bmi = вага / зріст 2 ).
# якщо bmi <= 18,5 повертає "Недостатня вага"
# якщо ІМТ <= 25,0 повертає "Нормальний"
# якщо ІМТ <= 30,0 повертає "Надмірна вага"
#endregion якщо ІМТ > 30, поверніть "Ожиріння"


user_weight = float(input("Put your own weight -->\n"))
user_height = float(input("Put your own height -->\n"))


user_imt = user_weight / user_height


if user_imt <= 18.5:
    print("Underweight")
elif user_imt == 25.0:
    print("Normal")
elif user_imt <= 30.0:
    print("Overweight")
elif user_imt > 30.0:
    print("Obese")