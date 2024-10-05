def duym(kilkist):
    return kilkist * 12
def yard(kilkist):
    return kilkist * 0.333333333
def mili(kilkist):
    return kilkist * 0.000189393939

user_q = int(input('Оберіть у яку одиницю вимірювання конвертуємо?\n1. Дюйми\n2. Ярди\n3. Милі\n> '))
kilkist = int(input('Введіть відстань у футах: '))

if user_q == 1:
    unit = "Дюйми"
    result = duym(kilkist)
elif user_q == 2:
    unit = "Ярди"
    result = yard(kilkist)
elif user_q == 3:
    unit = "Милі"
    result = mili(kilkist)
else:
    unit = "Такого не знайдено"
    result = "-"

unit_len = max(len("Одиниця вимірювання"), len(unit))
result_len = max(len("Значення"), len(str(result)))

podil = "." + "-" * (unit_len + 2) + "+" + "-" * (result_len + 2) + "."

print("\n" + podil)
print(f"| {'Одиниця вимірювання':<{unit_len}} | {'Значення':^{result_len}} |")
print(podil)

if result != "-":
    print(f"| {unit:<{unit_len}} | {result:^{result_len}} |")
else:
    print(f"| {unit:<{unit_len}} | {'-':^{result_len}} |")

print(podil)