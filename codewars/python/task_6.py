# Напиши програму, яка обчислює суму всіх цілих чисел від 1 до заданого числа n.


n = int(input("Put your number -->\n"))


if n < 1:
    print("Please enter a positive integer.")
while n > 1:
    n -= 1
    print(n)
while n == 1:
    break
