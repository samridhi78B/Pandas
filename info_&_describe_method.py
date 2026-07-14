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


#INFO METHOD-> SUMMARIZE TABLES, 
# RETURN DATATYPE, NON-NULL COUNT, COLUMN NAMES, MEMROY USAGE, NUMBER OF ROWS AND COLUMNS
df.info() 
# <class 'pandas.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    5 non-null      str  
#  1   Age     5 non-null      int64
#  2   Salary  5 non-null      int64
# dtypes: int64(2), str(1)
# memory usage: 252.0 bytes


#DESCRIBE->DESCRITPTIVE STAISTICS,-summary in numerical form
# MIN, MAX, MEAN, STD, 25%,50%,75%,NON-NULL COUNT
print(df.describe())
#           Age        Salary
# count   5.00000      5.000000
# mean   24.60000  69800.000000
# std     8.11172  32591.409911
# min    14.00000  22000.000000
# 25%    20.00000  50000.000000
# 50%    24.00000  89000.000000
# 75%    31.00000  90000.000000
# max    34.00000  98000.000000
