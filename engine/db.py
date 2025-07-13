import sqlite3
from engine.command import speak

def connect_db():
    conn = sqlite3.connect("sooha.db")
    cursor = conn.cursor()
    return cursor, conn

# create sys table 
# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# create web table 
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)


# insert into sys/web table function
def insert_command(message):
    message_split = message.split()

    type = message_split[1]
    name = message_split[2]
    size = len(message_split)

    speak("Adding " + type + " with name: " + name)

    if type == "path":
        query = "INSERT INTO sys_command VALUES (null, ?, ?)"
        path = ""
        for i in range(3, size):
            path += message_split[i] + " "
        cursor, conn = connect_db()
        cursor.execute(query, (name, path))
        conn.commit()
        conn.close()
    else:
        query = "INSERT INTO web_command VALUES (null, ?, ?)"
        url = ""
        for i in range(3, size):
            url += message_split[i] + " "
        cursor, conn = connect_db()
        cursor.execute(query, (name, url))
        conn.commit()
        conn.close()

def delete_command(message):
    message_split = message.split()

    type = message_split[1]
    name = message_split[2]

    speak("Deleting " + type + " with name: " + name)

    if type == "path":
        query = "DELETE FROM sys_command WHERE name=?"
        cursor, conn = connect_db()
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()
    else:
        query = "DELETE FROM web_command WHERE name=?"
        cursor, conn = connect_db()
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()

  








