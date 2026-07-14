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

print(df.head(3))
#    Name  Age  Salary
# 0   Arjun   34   50000
# 1   Palak   31   22000
# 2  Kanika   24   90000

print(df.tail(2))
#  Name  Age  Salary
# 3  Avni   14   89000
# 4   Sam   20   98000
