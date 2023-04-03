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


def view_pokemon():
    database = sqlConnect()
    db_cursor = database.cursor()
    db_cursor.execute("SELECT * FROM dragon_pokemon")
    dragonpokemons = db_cursor.fetchall()
    for dragonpokemon in dragonpokemons:
        print(dragonpokemon)


def update_pokemon():
    database = sqlConnect
    db_cursor = database.cursor()
    Pokemon = input("Enter pokemon: ")
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


def main():
    create_database()
    while True:
        print("1. Add pokemon\n2. View pokemon\n3. Update pokemon \n4. Delete pokemon\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_pokemon()
        elif choice == "2":
            view_pokemon()
        elif choice == "3":
            update_pokemon()
        elif choice == "4":
            delete_pokemon()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
