import sqlite3
import eel

def get_db_connection():
    conn = sqlite3.connect('sooha.db')
    conn.row_factory = sqlite3.Row  # This allows you to access columns by name
    return conn

def showdata():
    conn = get_db_connection()
    sys_commands = conn.execute('SELECT * FROM sys_command').fetchall()
    web_commands = conn.execute('SELECT * FROM web_command').fetchall()
    conn.close()

    # Display sys_command table data
    eel.receiverText("System Commands:")
    for command in sys_commands:
        str1 = str(dict(command))
        eel.receiverText(str1)
        

    # Display web_command table data
    eel.receiverText("Web Commands:")
    for command in web_commands:
        str1 = str(dict(command))
        eel.receiverText(str1)

