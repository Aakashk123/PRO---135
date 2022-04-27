import pandas as pd
import matplotlib.pyplot as mp

df = pd.read_csv ("filtered_stars")

print(df.head())

print(df.columns())


df.drop(['Unnamed: 0', 'Unnamed: 0.1'],axis=1,inplace=True)


# --------------------------------------------------------------------------------

name = df["Star_name"].to_list()

mass = df["Mass"].to_list()

radius = df["Radius"].to_list()

gravity = df["Gravity"].to_list()

dist = df["Distance"].to_list()

# ------------------------------------- Name VS mass ------------------------
mp.figure(figsize=(10,5))
mp.title("Solar Star Mass")

mp.bar(name[0:9] , mass[0:9])


# ------------------------------------- Name VS Radius ------------------------

mp.figure(figsize=(10,5))
mp.title("Solar Star Radius")

mp.bar(name[0:9] , radius[0:9])


# ------------------------------------- Name VS Gravity ------------------------

mp.figure(figsize=(10,5))
mp.title("Solar Star Gravity")

mp.bar(name[0:9] , gravity[0:9])


# ------------------------------------- Name VS Distance ------------------------

mp.figure(figsize=(10,5))
mp.title("Solar Star Distance")

mp.bar(name[0:9] , dist[0:9])






