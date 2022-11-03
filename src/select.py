from database.connection import execute_query
from pprint import pprint as pp

def select_all():
    query = """
        SELECT id, name FROM heroes
    """

    list_of_heroes = execute_query(query).fetchall()
    for record in list_of_heroes:
        pp(record)

# select_all()

def add_hero():
    name = input('What is the name of the hero being added to SQL Heroes?: ')
    about_me = input('Describe the hero in one line: ')
    bio = input('What is the inspiring backstory of this hero?: ')
    params = (name, about_me, bio)
    query = """
        INSERT INTO heroes (name, about_me, biography) VALUES(%s, %s, %s)
        """
    execute_query(query, params)

add_hero()

def remove_hero():
    select_all()
    whomst = input('Which hero is getting removed from SQL Heroes?: ')
    params = (whomst,)
    query = """
        DELETE FROM heroes WHERE id = %s
        """
    execute_query(query, params)
    select_all()

remove_hero()