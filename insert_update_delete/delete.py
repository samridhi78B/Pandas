import pandas as pd

data={
    "Name" : ["Arjun", "Palak", "Kanika", "Avni", "Sam"],
    "Age" : [34,31,24,14,20],
    "Salary" : [50000,22000,90000,89000,98000]
}

df=pd.DataFrame(data)

df.insert(0, "Employee_id",  [101,102,103,104,105])
print(df)
#    Employee_id    Name  Age  Salary   Bonus
# 0          101   Arjun   34   50000  5000.0
# 1          102   Palak   31   22000  2200.0
# 2          103  Kanika   24   90000  9000.0
# 3          104    Avni   14   89000  8900.0
# 4          105     Sam   20   98000  9800.0



#REMOVING DATA

# df.drop(columns = ["columnName"], inplace=True) #inplace=True (change the original data)

df.drop(columns=["Age"], inplace=True)
print(df)
#      Name    Salary   Bonus
# 0   Arjun   52500.0  5000.0
# 1   Palak  262500.0  2200.0
# 2  Kanika   94500.0  9000.0
# 3    Avni   93450.0  8900.0
# 4     Sam  102900.0  9800.0


#MULTIPLE COLUMNS REMOVE
df.drop(columns=["Salary", "Bonus"], inplace=True)
print(df)
#      Name
# 0   Arjun
# 1   Palak
# 2  Kanika
# 3    Avni
# 4     Sam
