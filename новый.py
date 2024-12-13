import functools

# Данные о рэперах
reps = [
    {"name": "Егор Крид", "age": 30, "albums": 11, "trecs": 222, "money": 55465466546},
    {"name": "Тимати", "age": 33, "albums": 13, "trecs": 345, "money": 865748},
    {"name": "Джони", "age": 21, "albums": 10, "trecs": 111, "money": 5748383},
    {"name": "Джарахов", "age": 40, "albums": 33, "trecs": 543, "money": 98474},
    {"name": "ДК", "age": 11, "albums": 40, "trecs": 987, "money": 8765432},
    {"name": "Билли Айлиш", "age": 29, "albums": 64, "trecs": 564, "money": 7675674},
    {"name": "Фараон", "age": 20, "albums": 54, "trecs": 786, "money": 4322334},
    {"name": "Токсис", "age": 19, "albums": 123, "trecs": 543, "money": 987665432},
    {"name": "Эминем", "age": 22, "albums": 23, "trecs": 33, "money": 456478},
    {"name": "Френдли Таг", "age": 25, "albums": 66, "trecs": 666, "money": 66666666}
]

# Данные о пользователях
users = {
    "админ": {"password": "админКрут", "role": "админ".lower()},
    "пользователь": {"password": "пользовательТут", "role": "Пользователь".lower()},
    "менеджер": {"password": "12345", "role": "менеджер".lower()}
}

def display_data(reps):
    print(f"{'Name':<20} {'Age':<5} {'Albums':<7} {'Tracks':<7} {'Money':<15}")
    print("-" * 60)
    for rapper in reps:
        print(f"{rapper['name']:<20} {rapper['age']:<5} {rapper['albums']:<7} {rapper['trecs']:<7} {rapper['money']:<15}")

def interface(users):
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if username in users and users[username]['password'] == password:
        return username
    else:
        print("Неверные учетные данные.")
        return None

def add_rapper(reps):
    name = input("Введите имя рэпера: ")
    while True:
        try:
            age = int(input("Введите возраст рэпера: "))
            albums = int(input("Введите количество альбомов: "))
            trecs = int(input("Введите количество треков: "))
            money = int(input("Введите количество денег: "))
            reps.append({"name": name, "age": age, "albums": albums, "trecs": trecs, "money": money})
            break
        except ValueError:
            print("Пожалуйста, введите корректное число для возраста, альбомов, треков и денег.")

def update_rapper(reps):
    name = input("Введите имя рэпера, которого хотите обновить: ")
    for rapper in reps:
        if rapper['name'] == name:
            while True:
                try:
                    age = int(input("Введите новый возраст рэпера: "))
                    albums = int(input("Введите новое количество альбомов: "))
                    trecs = int(input("Введите новое количество треков: "))
                    money = int(input("Введите новое количество денег: "))
                    rapper.update({"age": age, "albums": albums, "trecs": trecs, "money": money})
                    print(f"Информация о рэпере {name} успешно обновлена.")
                    return
                except ValueError:
                    print("Пожалуйста, введите корректное число для возраста, альбомов, треков и денег.")
    print(f"Рэпер с именем {name} не найден.")

def remove_rapper(reps):
    name = input("Введите имя рэпера, которого хотите удалить: ")
    reps[:] = [rapper for rapper in reps if rapper['name'] != name]

def filter_rep(reps):
    filters = {}

    age_limit = input("Введите минимальный возраст для фильтрации (или оставьте пустым): ")
    if age_limit:
        filters["age"] = int(age_limit)

    album_limit = input("Введите минимальное количество альбомов для фильтрации (или оставьте пустым): ")
    if album_limit:
        filters["albums"] = int(album_limit)

    track_limit = input("Введите минимальное количество треков для фильтрации (или оставьте пустым): ")
    if track_limit:
        filters["trecs"] = int(track_limit)

    filtered_reps = reps
    for key, value in filters.items():
        filtered_reps = [rep for rep in filtered_reps if rep[key] >= value]

    display_data(filtered_reps)

def sort_rep(reps):
    sorted_data = sorted(reps, key=lambda x: x['name'])
    display_data(sorted_data)

def search_rep(reps):
    search_name = input("Введите имя или часть имени рэпера для поиска: ").lower()
    found_reps = [rep for rep in reps if search_name in rep['name'].lower()]

    if found_reps:
        display_data(found_reps)
    else:
        print("Рэпер не найден.")

def podschet(reps):
    total_albums = functools.reduce(lambda x, y: x + y['albums'], reps, 0)
    total_tracks = functools.reduce(lambda x, y: x + y['trecs'], reps, 0)

    print(f"Общее количество альбомов: {total_albums}")
    print(f"Общее количество треков: {total_tracks}")

def user_menu():
    print("\nВыберите действие:")
    print("1. Просмотр всех рэперов")
    print("2. Фильтровать рэперов")
    print("3. Сортировать рэперов по имени")
    print("4. Поиск рэпера по имени")
    print("5. Подсчет треков и альбомов у всех рэперов")
    print("6. Выход")
    print("7. Обновить профиль")

def admin_menu():
    print("\nВыберите действие:")
    print("1. Просмотр всех рэперов")
    print("2. Добавить рэпера")
    print("3. Обновить информацию о рэпере")
    print("4. Удалить рэпера")
    print("5. Фильтровать рэперов")
    print("6. Сортировать рэперов по имени")
    print("7. Поиск рэпера по имени")
    print("8. Подсчет треков и альбомов у всех рэперов")
    print("9. Выход")
    print("10. Управление пользователями")

def update_profile(users, current_user):
    while True:
        print("\nВыберите действие:")
        print("1. Изменить пароль")
        print("2. Выход")
        choice = input("Ваш выбор: ")
        if choice == '1':
            new_password = input("Введите новый пароль: ")
            users[current_user]['password'] = new_password
            print("Пароль успешно изменен.")
        elif choice == '2':
            break
        else:
            print("Недостаточно прав доступа или неверный выбор.")

def manage_users(users):
    while True:
        print("\nВыберите действие:")
        print("1. Добавить пользователя")
        print("2. Удалить пользователя")
        print("3. Обновить информацию о пользователе")
        print("4. Выход")
        choice = input("Ваш выбор: ")
        if choice == '1':
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            role = input("Введите роль пользователя: ")
            users[username] = {'password': password, 'role': role}
            print("Пользователь успешно добавлен.")
        elif choice == '2':
            username = input("Введите имя пользователя, которого хотите удалить: ")
            if username in users:
                del users[username]
                print("Пользователь успешно удален.")
            else:
                print("Пользователь не найден.")
        elif choice == '3':
            username = input("Введите имя пользователя, которого хотите обновить: ")
            if username in users:
                password = input("Введите новый пароль: ")
                role = input("Введите новую роль пользователя: ")
                users[username] = {'password': password, 'role': role}
                print("Информация о пользователе успешно обновлена.")
            else:
                print("Пользователь не найден.")
        elif choice == '4':
            break
        else:
            print("Недостаточно прав доступа или неверный выбор.")

def main():
    current_user = interface(users)

    if current_user:
        user_role = users[current_user]['role']

        while True:
            if user_role == "пользователь":
                user_menu()
            else:
                admin_menu()
            choice = input("Ваш выбор: ")

            if user_role == "пользователь":
                if choice == '1':
                    display_data(reps)
                elif choice == '2':
                    filter_rep(reps)
                elif choice == '3':
                    sort_rep(reps)
                elif choice == '4':
                    search_rep(reps)
                elif choice == '5':
                    podschet(reps)
                elif choice == '6':
                    break
                elif choice == '7':
                    update_profile(users, current_user)
                else:
                    print("Недостаточно прав доступа или неверный выбор.")
            else:
                if choice == '1':
                    display_data(reps)
                elif choice == '2':
                    add_rapper(reps)
                elif choice == '3':
                    update_rapper(reps)
                elif choice == '4':
                    remove_rapper(reps)
                elif choice == '5':
                    filter_rep(reps)
                elif choice == '6':
                    sort_rep(reps)
                elif choice == '7':
                    search_rep(reps)
                elif choice == '8':
                    podschet(reps)
                elif choice == '9':
                    break
                elif choice == '10':
                    manage_users(users)
                else:
                    print("Недостаточно прав доступа или неверный выбор.")

if __name__ == "__main__":
    main()
