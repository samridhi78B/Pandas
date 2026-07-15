import pandas as pd

data={
    "Name" : ["Arjun", "Palak", "Kanika", "Avni", "Sam"],
    "Age" : [34,31,24,14,20],
    "Salary" : [50000,22000,90000,89000,98000]
}

df=pd.DataFrame(data)

#ORIGINAL DATA
#      Name  Age  Salary
# 0   Arjun   34   50000
# 1   Palak   31   22000
# 2  Kanika   24   90000
# 3    Avni   14   89000
# 4     Sam   20   98000


#UPDATION

#USING.loc() - SPECIFIC KO CHANGE KRNE KE LIYE

# df.loc[row_index, "column_name"] = new_value
df.loc[1, "Salary"] = 250000
print(df)
# 1   Palak   31  250000

# MULTIPLE VALUES KO UPDATE KRNE KE LIYE
df["Salary"] = df["Salary"] *1.05
print(df)

#     Name  Age    Salary
# 0   Arjun   34   52500.0
# 1   Palak   31  262500.0
# 2  Kanika   24   94500.0
# 3    Avni   14   93450.0
# 4     Sam   20  102900.0




