import random

secret = random.randint(1, 5)
x = 0
attempts = 0

while x != secret:
    x = int(input("Введите число от 1 до 5: "))
    attempts += 1  
    if attempts > 10:
        break
    if x > secret:
        print(f"{x} слишком велико")
    elif x < secret:
        print(f"{x} слишком мало")

if attempts > 10:
    print("Вы проиграли (превышен лимит попыток)")
else:
    print(f"Вы выиграли за {attempts} попыток!")