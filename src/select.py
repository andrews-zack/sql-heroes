from database.connection import execute_query
from pprint import pprint as pp

def list_heroes():
    query = """
        SELECT id, name
        FROM heroes;
        """
    list_of_heroes = execute_query(query).fetchall()
    for record in list_of_heroes:
        pp(record)


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
        SELECT DISTINCT
            heroes.id,
            heroes.name,
            heroes.about_me,
            heroes.biography,
            string_agg(ability_types.name, ' ')
        FROM heroes
        JOIN abilities ON heroes.id = abilities.hero_id
        JOIN ability_types ON ability_types.id = abilities.ability_type_id
        WHERE heroes.id = %s
        GROUP BY heroes.id;
    """
    hero_description = execute_query(query, params)
    for record in hero_description:
        pp(record)
    main_menu()


def see_abilities():
    query = """
            SELECT
                heroes.name,
                ability_types.name
            FROM heroes 
            JOIN abilities ON abilities.hero_id = heroes.id
            JOIN ability_types on abilities.ability_type_id = ability_types.id;
            """
    heroes_abilities = execute_query(query).fetchall()
    for record in heroes_abilities:
        pp(record)
    main_menu()


def see_relationships():
    query = """
        SELECT
            hero1.name,
            hero2.name,
            reltyp.name
        FROM relationship_types reltyp
        JOIN relationships rel ON reltyp.id = rel.relationship_type_id
        JOIN heroes hero1 on rel.hero1_id = hero1.id
        JOIN heroes hero2 ON rel.hero2_id = hero2.id;
    """
    hero_relationships = execute_query(query).fetchall()
    for record in hero_relationships:
        pp(record)
    # main_menu()


def add_hero():
    name = input('What is the name of the hero being added to SQL Heroes?: ')
    about_me = input('Describe the hero in one line: ')
    bio = input('What is the inspiring backstory of this hero?: ')
    params = (name, about_me, bio)
    query = """
        INSERT INTO heroes (name, about_me, biography) VALUES(%s, %s, %s);
        """
    execute_query(query, params)
    main_menu()


def remove_hero():
    list_heroes()
    whomst = input('Which hero is getting removed from SQL Heroes?: ')
    params = (whomst,)
    query = """
        DELETE FROM heroes WHERE id = %s;
        """
    execute_query(query, params)
    list_heroes()
    main_menu()


def change_relationship():
    see_relationships()
    first_choice = input("Enter the first hero of the relationship you would like to change: ")
    second_choice = input("Enter the second hero of the relationship you would like to change: ")
    first_id = get_id(first_choice)
    second_id = get_id(second_choice)
    params = (first_id, second_id)
    query = """
        UPDATE relationships
            IF relationships.hero1_id == %s AND relationships.hero2_id == %s
                SET relationship_type_id = 2;
    """
    execute_query(query, params)


def get_id(name):
    params = (name,)
    query = """
        SELECT id
        FROM heroes
        WHERE name = %s;
    """
    hero_id = execute_query(query, params).fetchall()
    return int(hero_id[0][0])


def change_name():
    list_heroes()
    hero_change = input("Which hero name would you like to change?: ")
    new_name = input("What is the hero's new name?: ")
    params = (new_name, hero_change )
    query = """
        UPDATE heroes
        SET name = %s
        WHERE id = %s;
    """
    execute_query(query, params)
    list_heroes()
    main_menu()


def main_menu():
    menu_list = {
        "See a hero": see_hero,
        "Add a hero": add_hero,
        "Remove a hero": remove_hero,
        "Friends list": see_relationships,
        "Change name": change_name,
        "See abilities": see_abilities,
        "Change relationship": change_relationship
    }
    for key in menu_list:
        print(key)
    choice = input("What do you want to do?: ")
    menu_list[choice]()


# def menu_input():
#     if input(""):
#         main_menu()


main_menu()