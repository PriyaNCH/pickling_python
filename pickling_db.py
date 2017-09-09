import pickle
import sqlite3
from sqlite3 import Error
from users import User


def create_db_connection():

    try:
        dbconn = sqlite3.connect('db.sqlite')
        return dbconn
    except Error as e:
        print(e)

    return None


def close_db_connection(dbconn):
    dbconn.close()


def create_sqlite_db(dbconn, user_data):

    cursor = dbconn.cursor()

    cursor.execute(
        'CREATE TABLE USER (user_id INTEGER PRIMARY KEY,user_data BLOB)')
    query = "INSERT INTO USER (user_data) VALUES (?)"
    pickledData = pickle.dumps(user_data)
    cursor.execute(query, (pickledData,) )

    print("User inserted")

    dbconn.commit()


def read_from_db(dbconn):

    cursor = dbconn.cursor()
    
    cursor.execute('SELECT user_data FROM USER')
    rows = cursor.fetchall()
    for row in rows:
        for original_data in row:
            unpickled_data = pickle.loads(original_data)
            print("Data after loading from db")
            print(unpickled_data)

            return unpickled_data

def get_user_info():
    user1 = User("VP","Swiss", "WD", ["Watching TV", "Dance", "Music", "Reading Books"])

    user2 = User("TC", "Aus", "SD", ["Watching TV", "Sleep", "Coding", "Reading Books"])

    count = user2.getUserCount()
    user_history = {user1.name: user1, user2.name : user2, 'count' : count}
    print("original data")
    print(user_history)

    return user_history

user_info = get_user_info()
dbconn = create_db_connection()
create_sqlite_db(dbconn, user_info)
user_info_db = read_from_db(dbconn)
print(user_info == user_info_db)
close_db_connection(dbconn)

#https://stackoverflow.com/questions/30469575/how-to-pickle-and-unpickle-to-portable-string-in-python-3