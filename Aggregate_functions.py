import pandas as pd
data = {
    "Name" : ['Samridhi', 'Avni', 'Kanika', 'Ajay'],
    "Age" : [22, 14, 25,34],
    "Salary" : [400000, 350000, 980000, 100000000]
}
df=pd.DataFrame(data)
avg_age=df["Age"].mean()
print(avg_age) #23.75

sum_age=df["Age"].sum()
print(sum_age) #95

std_age=df["Age"].std()
print(std_age) #8.261355820929152

min_age=df["Age"].min()
print(min_age) #14

max_age=df["Age"].max()
print(max_age) #34
