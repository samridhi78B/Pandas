import pandas as pd

data={
    "Name" : ["Arjun", "Palak", "Kanika", "Avni", "Sam"],
    "Age" : [34,31,24,14,20],
    "Salary" : [50000,22000,90000,89000,98000]
}

df=pd.DataFrame(data)

print(df) 
#      Name  Age  Salary
# 0   Arjun   34   50000
# 1   Palak   31   22000
# 2  Kanika   24   90000
# 3    Avni   14   89000
# 4     Sam   20   98000

#SHAPE-RETURN ROWS AND COLUMNS
print(df.shape) 
# (5, 3)


#COLUMNS-RETURN COLUMN NAMES
print(df.columns) 
# Index(['Name', 'Age', 'Salary'], dtype='str')



#ACESSING COLUMNS
#SELECT SPECIIFC COLUMN - USE SQUARE BRACKETS
#It will return a series (single column)
#Dataframe if multiple columns

col = df["Name"]
print(col)
# 0     Arjun
# 1     Palak
# 2    Kanika
# 3      Avni
# 4       Sam
# Name: Name, dtype: str

#Dataframe if multiple columns
mul_col = df[["Name", "Salary" ]]
print(mul_col)
#      Name  Salary
# 0   Arjun   50000
# 1   Palak   22000
# 2  Kanika   90000
# 3    Avni   89000
# 4     Sam   98000


#FILTER ROWS 
# use boolean expression
filtered_rows = df[df["Salary"] < 70000]
print(filtered_rows)
#     Name  Age  Salary
# 0  Arjun   34   50000
# 1  Palak   31   22000


#USING MULTIPLE CONDITIONS 
fil_rows = df [(df["Salary"] > 22000) & (df["Age"] > 20)]
print(fil_rows)
#      Name  Age  Salary
# 0   Arjun   34   50000
# 2  Kanika   24   90000
