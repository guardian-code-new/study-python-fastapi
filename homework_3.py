print('Умовні конструкції:')
print('1. Перевірка паролю:')
user_1 = {
    "user_name": "Name 1",
    "password": "password123"
}

if "password123" in user_1["password"]:
    print("Ви увійшли в систему!")
else:
    print("Неправильний пароль")

print('2. Визначення днів тижня:')
days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
lst = [1, 2, 3,]
if lst[0] >= 1 and lst[0] <= 7:
    print(days_of_week[lst[0]])
else:
    print("Wrong day number")

print('Цикли:')
print('1. Таблиця множення:')
calc_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in calc_list:
    print(f"{6} * {n} = {6 * n}")

print('2. Сума чисел:')
sum_list = 0
for s in calc_list:
    sum_list += s
    print(sum_list)

print('3. Факторіал числа:')
fct = 1

for fa in calc_list:
    fct *= fa
    print(fct)

print('4. Парні числа:')
for num in range(1, 51):
    if num % 2 == 0:
        print(num)

print('5. Пошук простих чисел:')
list_51 = []

for x in range(2, 51):
    for y in list_51:
        if x % y == 0:
            break
    else:
        list_51.append(x)
print(list_51)

