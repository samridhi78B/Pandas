import pandas as pd
data = {
    "Name" : ['Samridhi', 'Avni', 'Kanika', 'Ajay'],
    "Age" : [22, 14, 25,34],
    "Salary" : [400000, 350000, 980000, 100000000]
}
df=pd.DataFrame(data)
#SORT BY ASCENDING ORDER - A SINGLE COLUMN
df.sort_values(by="Age", ascending=True ,inplace=True)
print(df)
#        Name  Age     Salary
# 1      Avni   14     350000
# 0  Samridhi   22     400000
# 2    Kanika   25     980000
# 3      Ajay   34  100000000


#SORT BY DESCENDING - MULTIPLE COLUMNS
df.sort_values(by=["Age", "Salary"], ascending=[False, False], inplace=True)
print(df)
#       Name  Age     Salary
# 3      Ajay   34  100000000
# 2    Kanika   25     980000
# 0  Samridhi   22     400000
# 1      Avni   14     350000


