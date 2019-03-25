from pyhive import hive
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


cols = ['DexNumber', 'abilities', 'against_bug', 'against_dark', 'against_dragon',
        'against_electric', 'against_fairy', 'against_fight', 'against_fire',
        'against_flying', 'against_ghost', 'against_grass', 'against_ground',
        'against_ice', 'against_normal', 'against_poison', 'against_psychic',
        'against_rock', 'against_steel', 'against_water', 'attack',
        'base_egg_steps', 'base_happiness', 'base_total', 'capture_rate',
        'classfication', 'defense', 'experience_growth', 'height_m', 'hp',
        'japanese_name', 'name', 'percentage_male', 'pokedex_number',
        'sp_attack', 'sp_defense', 'speed', 'type1', 'type2', 'weight_kg',
        'generation', 'is_legendary']


def display(cursor):
    result = []
    while(True):
        try:
            result.append((cursor.next()))
        except StopIteration:
            print("Loading done")
            break
    return pd.DataFrame(result, columns=cols)


cursor = hive.connect('localhost').cursor()

cursor.execute("DROP table Pokemon")
cursor.execute("create table pokemon (\
DexNumber INT, Abilities string, against_bug FLOAT, against_dark FLOAT, against_dragon FLOAT,\
against_electric FLOAT, against_fairy FLOAT, against_fight FLOAT, against_fire FLOAT, \
against_flying FLOAT, against_ghost FLOAT, against_grass FLOAT, against_ground FLOAT,\
against_ice FLOAT, against_normal FLOAT, against_poison FLOAT,  against_psychic FLOAT,\
against_rock FLOAT, against_steel FLOAT, against_water FLOAT, attack int,\
base_egg_steps int, base_happiness int, base_total int, capture_rate string,\
classfication string, defense int, experience_growth int, height_m FLOAT, hp int,\
japanese_name string, name string , percentage_male FLOAT, pokedex_number int,\
sp_attack int, sp_defense int, speed int, type1 string, type2 string, weight_kg FLOAT,\
generation int , is_legendary int) row format delimited fields terminated by ','")

cursor.execute("load data local inpath 'pokemon.txt' into table Pokemon")


# View the first 5 rows of the DataSet
cursor.execute("Select * from pokemon LIMIT 5")
display(cursor)

# View the last 5 rows of the DataSet
cursor.execute("Select * from pokemon ORDER BY Number DESC LIMIT 5")
display(cursor)


df = pd.read_csv("pokemon.csv")
columns = df.columns
