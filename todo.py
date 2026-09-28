tasks = []


def add_task():
    text = input("Введите текст задачи: ").strip()
    if not text:
        print("Задача не может быть пустой!")
        return
    tasks.append(text)
    print("Задача добавлена!")


def show_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task():
    if not tasks:
        print("Список задач пуст, удалять нечего.")
        return
    show_tasks()
    try:
        number = int(input("Введите номер задачи для удаления: "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Задача «{removed}» удалена.")
    else:
        print("Задачи с таким номером нет.")


def main():
    while True:
        print("\n--- Список задач ---")
        print("1. Добавить задачу")
        print("2. Показать список задач")
        print("3. Удалить задачу")
        print("4. Выход")
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню. Введите число от 1 до 4.")


if __name__ == "__main__":
    main()