# 1
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

# 2
shopping_list = ["яблоко", "молоко", "хлеб", "яблоко", "масло", "яйца", "молоко"]
unique_items = set(shopping_list)
print(len(set(shopping_list)))

# 3
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
print(seasons_dict)

# 4
users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
statistics = {"Общее количество": 0, "Уникальные посещения": 0}
statistics["Общее количество"] = len(users)
unique_users = set(users)
statistics["Уникальные посещения"] = len(unique_users)
print(statistics)

# 5
list_participants = ["Орлов", "Петров", "Иванов", "Сидоров", "Васильев", "Черепахин"]
print(f"Last: {list_participants[-1]}\nFirst: {list_participants[0]}")

# 6
sps = ["Дубровский", "Горе от ума", "Кавказский пленник", "Хамелеон", "Ревизор", "Гранатовый браслет"]
print(len(sps))

#7
shopping_list = ["Палатка", "Спальник", "Котелок", "Тренога", "Рюкзак", "Спальник", "Рюкзак", "Термос", "Миска", "Ветровка", "Коврик"]
print(len(shopping_list))


