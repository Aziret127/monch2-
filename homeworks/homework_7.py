import sqlite3

def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
     )
     """)
def add_book(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    conn.commit()
if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    create_table(conn)
    add_book(conn,"Война и мир", "Лев Толстой", "1869", "Исторический роман", "1225", "6")
    add_book(conn,"<<1984>>","ДжорджОруэлл","1949","Антиутопия / политический роман","328", "8")
    add_book(conn,"гордость и предубеждение","Фёдор Достоевский","1866","психологический роман","279","5")
    add_book(conn,"приступление и наказание","Ф.Скотт Фицджеральд","1925","Социальный роман / трагедия","180","10")
    add_book(conn,"Сто лет одиночества","Габриэль Гарсиа Маркес","1967","Магический реализм","417","4")
    add_book(conn,"Убить пересмешника","Харпер Ли","1960","Социально-психологический роман","281","9")
    add_book(conn,"Над пропастью во ржи","Дж. Д. Сэлинджер","1951","Роман взросления","234","12")
    add_book(conn,"Моби Дик» ","Герман Мелвилл","1851","Приключенческий роман / эпопея","695","3")
    add_book(conn,"Хоббит, или Туда и обратно","Дж. Р. Р. Толкин","1937","Фэнтези","310","11")
    add_book(conn,"Великий Гэтсби","Ф. Скотт Фицджеральд","1925","Социальный роман / трагедия","180","10")