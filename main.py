import mysql.connector
from decouple import config


def sqlConnect():  # connects to the db
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=config("password"),
        database="pokemon",
        auth_plugin="mysql_native_password"
    )


def create_database():  # creates dragon_pokemon table with 6 columns
    database = sqlConnect()
    db_cursor = database.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS dragon_pokemon (id int AUTO_INCREMENT PRIMARY KEY, Pokemon VARCHAR(255), FastMove VARCHAR(255), ChargeMove VARCHAR(255), DPS float, TDO float, Total float)")
    db_cursor.execute("SELECT * FROM dragon_pokemon")


# prompts the user to enter values of each column created such as Pokemon name, moves, dps etc.
def add_pokemon():
    database = sqlConnect()
    db_cursor = database.cursor()
    Pokemon = input("Enter Pokemon: ")
    FastMove = input("Enter Fast Move: ")
    ChargeMove = input("Enter Charge Move: ")
    DPS = input("Enter DPS: ")
    TDO = input("Enter TDO: ")
    Total = input("Enter Total: ")
    db_cursor.execute("INSERT INTO dragon_pokemon (Pokemon, FastMove, ChargeMove, DPS, TDO, Total) VALUES (%s, %s, %s,%s, %s, %s)",
                      (Pokemon, FastMove, ChargeMove, DPS, TDO, Total))
    database.commit()
    print(db_cursor.rowcount, "record inserted")


def view_pokemon():  # retrieves all records from dragon_pokemon using SELECT and fetchall()
    database = sqlConnect()
    db_cursor = database.cursor()
    db_cursor.execute("SELECT * FROM dragon_pokemon")
    dragonpokemons = db_cursor.fetchall()
    for dragonpokemon in dragonpokemons:
        print(dragonpokemon)


def update_pokemon():  # prompts the user to enter new values to each column from a specified id
    database = sqlConnect()
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


def delete_pokemon():  # delete a pokemon record from the table using inserting it's id
    database = sqlConnect()
    db_cursor = database.cursor()
    id = input("Enter id: ")
    db_cursor.execute("DELETE FROM dragon_pokemon WHERE id = %s", (id,))
    database.commit()
    print(db_cursor.rowcount, "record(s) deleted")


def main():  # calls create database and display a menu of options for the user to choose whether he/she wants to add, view, update, delete or exit
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


if __name__ == "__main__":  # main is only executed if the script is run directly
    main()
