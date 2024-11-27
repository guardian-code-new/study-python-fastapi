print("Списки:\n1. Робота із списками:")
num_list = [1, 2, 3, 4, 5, 6]
num_list.extend([10, 20])
print(num_list)
num_list.pop(6)
print(num_list)

print("2. Знаходження суми:")
print(sum(num_list))

print("3. Подвійні значення:")
for x in num_list:
    dobl = x * 2
    print(f"2 * {x} = {dobl}")

print("Кортежі:\n1. Робота із кортежами:")
cott_1 = ("apple", "banana", "orange")
print(cott_1[0], cott_1[1], cott_1[2])

print("2. Об'єднання кортежів:")
cott_2 = (1, 3, 5, 7)
new_cott = cott_1 + cott_2
print(new_cott)

print("Словники:\n1. Робота із словниками:")
sportsman = {
    "name": "Usain",
    "age": 38,
    "sport": "Athletic",
    "distance": "sprint"
}
print(sportsman["name"], sportsman["age"], sportsman["sport"], sportsman["distance"])
print(sportsman.get("name"), sportsman.get("age"), sportsman.get("sport"), sportsman.get("distance"))

print("2. Оновлення словника:")
books = {
    "name1": "The Richest Man in Babylon",
    "publication1": 1926
}
books.update({"name2": "Think and Grow Rich", "publication2": 1937})
print(books)

print("3. Пошук значення:")

