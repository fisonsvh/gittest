import sqlite3

con = sqlite3.connect('emails.sqlite')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Emails  (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE

)
''')



while True:
    email = input("Enter your email: ").capitalize()
    name = input("Enter your name: ").capitalize()
    cur.execute("INSERT INTO Emails (name, email) VALUES (?, ?)", email, name)


con.commit()
con.close()

# cursor.executemany("INSERT INTO Users(name, email) VALUES (?, ?)", users)
# INSERT INTO Users (name, email) VALUES ('John Doe', 'john@gmail.com');
# INSERT INTO Users (name, email) VALUES ('Nick Sand', 'sand@gmail.com');
# ''')


# def dict_factory(cur, row):
#     d = {}
#     for idx, col in enumerate(cur.description):
#         d[col[0]] = row[idx]
#     return d

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE
# )
# ''')  # Создание таблицы


#
# con = sqlite3.connect('tes_db.sqlite')
# con.row_factory = dict_factory
# cur = con.cursor()
#
# cur.execute("SELECT * FROM Users")
# print(cur.fetchall(), sep= '\n')
# con.close()

# email = input('Enter your e-mail: ').capitalize()
# cursor.execute(f"SELECT * FROM Users WHERE EMAIL = '{email}'")

# cursor.execute("SELECT * FROM Users WHERE email = :email OR name = :name", {'email': email, 'name' : 'Fisochenko Vladyslav'} )
# res = cursor.fetchone()


# for user in res:
#     print(user[0], user[1], user[2])
#


# cursor.execute("INSERT INTO Users (name, email) VALUES ('Fisochenko Vladyslav', 'Fison23@gmail.com')")
# cursor.execute("INSERT INTO Users (name, email) VALUES ('Vika Navrotska', 'Navro@gmail.com')")
#
# cursor.executescript('''
# INSERT INTO Users (name, email) VALUES ('John Doe', 'john@gmail.com');
# INSERT INTO Users (name, email) VALUES ('Nick Sand', 'sand@gmail.com');
# ''')

# users = [
#     ('User1', 'user1@gmail.com'),
#     ('User2', 'user2@gmail.com'),
#     ('User3', 'user3@gmail.com')
# ]
#
# cursor.executemany("INSERT INTO Users(name, email) VALUES (?, ?)", users)
#
# conn.commit()
