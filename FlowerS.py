#Коллекция товаров
flowers = [
    {"name": "Розы", "price": 1000, "occasion": "свадьба", "description": "Красные розы, 12 штук"},
    {"name": "Тюльпаны", "price": 600, "occasion": "день рождения", "description": "Яркие тюльпаны, 10 штук"},
    {"name": "Лилии", "price": 1200, "occasion": "юбилей", "description": "Белые лилии, 5 штук"},
    {"name": "Хризантемы", "price": 800, "occasion": "свидание", "description": "Жёлтые хризантемы, 7 штук"},
    {"name": "Орхидеи", "price": 1500, "occasion": "свадьба", "description": "Фиолетовые орхидеи, 3 штуки"},
    {"name": "Пионы", "price": 900, "occasion": "день рождения", "description": "Розовые пионы, 6 штук"},
    {"name": "Герберы", "price": 700, "occasion": "свидание", "description": "Яркие герберы, 8 штук"},
    {"name": "Ирисы", "price": 500, "occasion": "юбилей", "description": "Синие ирисы, 9 штук"},
    {"name": "Гвоздики", "price": 400, "occasion": "день рождения", "description": "Красные гвоздики, 10 штук"},
    {"name": "Подсолнухи", "price": 750, "occasion": "свидание", "description": "Солнечные подсолнухи, 5 штук"},
]

purchase_history = []
occasions = set(flower["occasion"] for flower in flowers)

#Функция отображения всех цветов
def show_all_flowers():
    print("\nВсе цветы в магазине:")
    for idx, flower in enumerate(flowers, 1):
        print(f"{idx}. {flower['name']} - {flower['price']} руб. ({flower['description']})")

#Функция рекомендации цветов по поводу
def recommend_flowers(occasion):
    print(f"\nРекомендуемые цветы для повода '{occasion}':")
    found = False
    for idx, flower in enumerate(flowers, 1):
        if flower["occasion"] == occasion:
            print(f"{idx}. {flower['name']} - {flower['price']} руб. ({flower['description']})")
            found = True
    if not found:
        print("Цветы для этого повода не найдены.")

#Функция пополнения баланса
def add_balance(balance):
    try:
        amount = int(input("Введите сумму для пополнения: "))
        if amount > 0:
            balance += amount
            print(f"Баланс успешно пополнен. Текущий баланс: {balance} руб.")
        else:
            print("Сумма должна быть больше 0.")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите число.")
    return balance

#Функция обработки покупки
def process_purchase(choice, balance):
    if 0 < choice <= len(flowers):
        flower = flowers[choice - 1]
        if balance >= flower["price"]:
            print(f"\nВы выбрали: {flower['name']} ({flower['description']})")
            balance -= flower["price"]
            print(f"Ваш остаток: {balance} руб.")
            purchase_history.append(flower)
            return balance
        else:
            print("\nНедостаточно средств. Пожалуйста, пополните баланс.")
            return balance
    else:
        print("\nНеверный выбор. Пожалуйста, выберите цветок из меню.")
        return balance

#Основная функция
def flower_shop():
    balance = 0
    while True:
        print("\nГлавное меню:")
        print("1. Показать все цветы")
        print("2. Рекомендовать цветы по поводу")
        print("3. Пополнить баланс")
        print("4. Показать историю покупок")
        print("0. Выйти")
        
        try:
            menu_choice = int(input("Выберите действие: "))
            if menu_choice == 0:
                print("\nСпасибо за использование нашего магазина! До свидания!")
                print("История ваших покупок:")
                for purchase in purchase_history:
                    print(f"- {purchase['name']} ({purchase['price']} руб.)")
                break
            elif menu_choice == 1:
                show_all_flowers()
                try:
                    choice = int(input("Выберите цветок (введите номер) или 0 для возврата: "))
                    if choice != 0:
                        balance = process_purchase(choice, balance)
                except ValueError:
                    print("Ошибка ввода. Пожалуйста, введите номер цветка.")
            elif menu_choice == 2:
                print("\nДоступные поводы:", ", ".join(occasions))
                occasion = input("Введите повод для рекомендации: ")
                if occasion in occasions:
                    recommend_flowers(occasion)
                    try:
                        choice = int(input("Выберите цветок (введите номер) или 0 для возврата: "))
                        if choice != 0:
                            balance = process_purchase(choice, balance)
                    except ValueError:
                        print("Ошибка ввода. Пожалуйста, введите номер цветка.")
                else:
                    print("Повод не найден.")
            elif menu_choice == 3:
                balance = add_balance(balance)
            elif menu_choice == 4:
                if purchase_history:
                    print("\nИстория покупок:")
                    for purchase in purchase_history:
                        print(f"- {purchase['name']} ({purchase['price']} руб.)")
                else:
                    print("\nИстория покупок пуста.")
            else:
                print("\nНеверный выбор. Пожалуйста, выберите действие из меню.")
        except ValueError:
            print("\nОшибка ввода. Пожалуйста, введите число.")

if __name__ == "__main__":
    flower_shop()