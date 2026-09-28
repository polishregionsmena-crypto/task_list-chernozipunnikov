tasks = []


def add_task():
    text = input("Введите текст задачи: ")
    tasks.append(text)
    print("Задача добавлена!")


def show_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def main():
    while True:
        print("\n--- Список задач ---")
        print("1. Добавить задачу")
        print("2. Показать список задач")
        print("3. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")


main()