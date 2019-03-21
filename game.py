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


# DO NOT Modify the following code. Start work from here:

df = pd.read_csv('Pokemon.csv')

# Your code here
