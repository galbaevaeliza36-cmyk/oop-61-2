import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS films (
        name TEXT,
        genre TEXT,
        rating INTEGER
    )
''')
connect.commit()


def create_films(name, genre, rating):
    cursor.execute(
        'INSERT INTO films VALUES (?, ?, ?)',
        (name, genre, rating)
    )
    connect.commit()
    print(f'Фильм добавлен: {name}!')


create_films("Dear X", "Thriller", 1)
connect.commit()

def get_films():
    cursor.execute('SELECT * FROM films')
    films = cursor.fetchall()
    # print(films)
    for i in films:
        print (f'NAME: {i[0]}, GENRE: {i[1]}, RATING: {i[2]}')

# get_films()
# def update_films_name(rating, name):
#     cursor.execute(
#         'UPDATE films SET name = ? WHERE rating = ?',
#         (name, rating)
def update_films_name(row_id, name):
    cursor.execute(
        'UPDATE films SET name = ? WHERE rowid = ?',
        (name, row_id)
    )
    connect.commit()
    print("Фильм обновлён!!!")
update_films_name(3, "Cheer up")

def delete_films(row_id):
    cursor.execute(
        'DELETE FROM films WHERE rowid =? ',
        (row_id,)
    )
    connect.commit()
    print ("Фильм удален !")

delete_films(4)