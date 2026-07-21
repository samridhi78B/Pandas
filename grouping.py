import pandas as pd
data = {
    "Name" : ['Samridhi', 'Avni', 'Kanika', 'Ajay'],
    "Age" : [14, 14, 25,14],
    "Salary" : [400000, 350000, 980000, 100000000]
}
df=pd.DataFrame(data)

res=df.groupby("Age")["Salary"].sum()
print(res) 
#Age
# 14    100750000
# 25       980000

result = df.groupby(["Age", "Name"])["Salary"].sum()
print(result)
# 14   Ajay        100000000
#      Avni           350000
#      Samridhi       400000
# 25   Kanika         980000
