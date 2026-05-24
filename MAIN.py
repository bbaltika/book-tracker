import json
import os
from datetime import datetime

dafileta = "books.json"

def load_books():
    if not os.path.exists(dafileta):
        return []
    with open(dafileta, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def is_duplicate(books, author, title):
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            return True
    return False

def add_book(books):
    print("\nДобавление книги")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    if not author or not title:
        print("Ошибка: автор и название не могут быть пустыми.")
        return

    if is_duplicate(books, author, title):
        print("Ошибка: такая книга уже есть.")
        return

    try:
        rating = int(input("Оценка (1-5): ").strip())
        if rating < 1 or rating > 5:
            print("Ошибка: оценка должна быть от 1 до 5.")
            return
    except ValueError:
        print("Ошибка: введите целое число.")
        return
    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date_str
    })
    save_books(books)
    print("Книга успешно добавлена!")

def show_all_books(books):
    print("\nСписок книг")
    if not books:
        print("Нет добавленных книг.")
        return
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book['author']} — «{book['title']}», оценка: {book['rating']}, прочитано: {book['date']}")

def show_average_rating(books):
    if not books:
        print("Нет книг для расчёта средней оценки.")
        return
    total = sum(book['rating'] for book in books)
    avg = total / len(books)
    print(f"\nСредняя оценка всех книг: {avg:.2f}")

def author_statistics(books):
    if not books:
        print("Нет книг для статистики.")
        return
    stats = {}
    for book in books:
        author = book['author']
        stats[author] = stats.get(author, 0) + 1
    print("\nСтатистика по авторам")
    for author, count in stats.items():
        print(f"{author}: {count} книг(а)")

def delete_book(books):
    if not books:
        print("Нет книг для удаления.")
        return
    show_all_books(books)
    try:
        idx = int(input("\nВведите номер книги для удаления: ").strip())
        if 1 <= idx <= len(books):
            removed = books.pop(idx - 1)
            save_books(books)
            print(f"Книга «{removed['title']}» удалена.")
        else:
            print("Ошибка: неверный номер.")
    except ValueError:
        print("Ошибка: введите число.")

def main():
    books = load_books()
    while True:
        print("\nТрекер прочитанных книг")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            add_book(books)
            books = load_books() 
        elif choice == "2":
            show_all_books(books)
        elif choice == "3":
            show_average_rating(books)
        elif choice == "4":
            author_statistics(books)
        elif choice == "5":
            delete_book(books)
            books = load_books()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный пункт, попробуйте снова.")

if __name__ == "__main__":
    main()
