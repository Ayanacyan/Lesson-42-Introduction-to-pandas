import pandas as pd

scores= pd.Series([1520, 1005, 980, 3, -400], index=["Alex", "Summer", "Adam", "Selene", "Ayana"])
print("Top player scores")
print(scores)

data={
    "Player":["Alex", "Summer", "Adam", "Selene", "Ayana"],
    "Score":[1520, 1005, 980, 3, -400],
    "Level":[9, 20, 47, 8, 1000],
    "Wins":[35, 600, 59, -50, 3 ]
}
df=pd.DataFrame(data)
print("Gaming Leaderboard")
print(df)

print("First Player")
print(df.loc[0])

print("First three players")
print(df.loc[0:2])

cs=pd.read_csv("leaderboard.csv")
print("First five rows")
print(cs.head())

print("Last five rows")
print(cs.tail())

print("Data set information")
cs.info()
