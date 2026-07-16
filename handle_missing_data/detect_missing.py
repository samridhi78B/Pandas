import pandas as pd
 #HOW TO DETECT MISSING VALUES
#USE .isnull() -> to detect missing values

data= {
    "Name" : ['Ram', None, 'Avni', 'Kanika', 'Sam'],
    "Age" : [10,20,None,16,23],
    "Salary" : [20000, 30000, 15000,340000, None]
}
df=pd.DataFrame(data)

print(df.isnull())
#     Name    Age  Salary
# 0  False  False   False
# 1   True  False   False
# 2  False   True   False
# 3  False  False   False
# 4  False  False    True

print(df.isnull().sum()) #COUNT OF NULL VALUES IN EVERY COLUMN
# Name      1
# Age       1
# Salary    1
# dtype: int64
