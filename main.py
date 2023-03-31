import mysql.connector


def sqlConnect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="q0fmUEe16wNq)~2G",
        database="PokemonPy",
        auth_plugin="mysql_native_password"
    )


def create_database():
    database = sqlConnect()
    db_cursor = database.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS dragon_pokemon (id int AUTO_INCREMENT PRIMARY KEY, Pokemon VARCHAR(255), FastMove VARCHAR(255), ChargeMove VARCHAR(255), DPS float, TDO float, Total float)")
    db_cursor.execute("SELECT * FROM dragon_pokemon")


def add_pokemon():
    database = sqlConnect()
    db_cursor = database.cursor()
    Pokemon = input("Enter Pokemon: ")
    FastMove = input("Enter Fast Move: ")
    ChargeMove = input("Enter Charge Move: ")
    DPS = input("Enter DPS: ")
    TDO = input("Enter TDO: ")
    Total = input("Enter Total: ")
    db_cursor.execute("UPDATE dragon_pokemon SET Pokemon = %s, FastMove = %s, ChargeMove = %s, DPS = %s, TDO = %s, Total = %s WHERE id = %s",
                      (Pokemon, FastMove, ChargeMove, DPS, TDO, Total, id))
    database.commit()
    print(db_cursor.rowcount, "record(s) affected")


def delete_pokemon():
    database = sqlConnect()
    db_cursor = database.cursor()
    id = input("Enter id: ")
    db_cursor.execute("DELETE FROM dragon_pokemon WHERE id = %s", (id))
    database.commit()
    print(db_cursor.rowcount, "record(s) deleted")
