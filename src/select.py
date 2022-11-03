from database.connection import execute_query
from pprint import pprint as pp

def see_hero():
    query1 = """
        SELECT id, name from heroes
        """
    list_of_heroes = execute_query(query1).fetchall()
    for record in list_of_heroes:
        pp(record)
    which_hero = input("Which hero record would you like to view?: ")
    params = (which_hero,)
    query = """
        SELECT name, about_me, biography
        FROM heroes
        WHERE id = %s
    """
    execute_query(query, params)
    pp(query)
    main_menu()


# see_hero()

def add_hero():
    name = input('What is the name of the hero being added to SQL Heroes?: ')
    about_me = input('Describe the hero in one line: ')
    bio = input('What is the inspiring backstory of this hero?: ')
    params = (name, about_me, bio)
    query = """
        INSERT INTO heroes (name, about_me, biography) VALUES(%s, %s, %s)
        """
    execute_query(query, params)
    main_menu()

# add_hero()

def remove_hero():
    select_all()
    whomst = input('Which hero is getting removed from SQL Heroes?: ')
    params = (whomst,)
    query = """
        DELETE FROM heroes WHERE id = %s
        """
    execute_query(query, params)
    select_all()
    main_menu()

# remove_hero()

def main_menu():
    menu_list = {
        "See a hero": see_hero,
        "Add a hero": add_hero,
        "Remove a hero": remove_hero
    }
    for key in menu_list:
        print(key)
    choice = input("What do you want to do?: ")
    menu_list[choice]()

main_menu()
