from pyhive import hive
import matplotlib.pyplot as plt
import pandas as pd


cursor = hive.connect('localhost').cursor()

cursor.execute("DROP table Pokemon")
cursor.execute("create table pokemon\
(Number int, Name String, Type1 String, Type2 String,\
Total String, HP int, Attack int, Defense int, Sp_Atk int,\
  Sp_Def int, Speed int, Generation int, Legendary Boolean)\
  row format delimited fields terminated by ','")

cursor.execute("load data local inpath 'Pokemon.txt' into table Pokemon")
cursor.execute("Select * from pokemon")

pokemon = []
while(True):
    try:
        pokemon.append((cursor.next()))
    except StopIteration:
        print("Loading done")
        break

len(pokemon)

# DO NOT Modify the following code. Start work from here:
# TODO: Use Seaborn and Matplotlib to analyse the dataset.
# Once you are done, I will swap the pandas queries for hive queries.
df = pd.read_csv('Pokemon.csv')
