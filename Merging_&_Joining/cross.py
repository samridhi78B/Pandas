import pandas as pd
employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104],
    "Name": ["Aman", "Riya", "Karan", "Neha"],
    "Department_ID": [1, 2, 3, 2]
})

departments = pd.DataFrame({
    "Department_ID": [1, 2, 4],
    "Department_Name": ["HR", "IT", "Finance"]
})

res=pd.merge(employees, departments, how="cross") #DONT USE ON 
print(res)
#     Emp_ID   Name  Department_ID_x  Department_ID_y Department_Name
# 0      101   Aman                1                1              HR
# 1      101   Aman                1                2              IT
# 2      101   Aman                1                4         Finance
# 3      102   Riya                2                1              HR
# 4      102   Riya                2                2              IT
# 5      102   Riya                2                4         Finance
# 6      103  Karan                3                1              HR
# 7      103  Karan                3                2              IT
# 8      103  Karan                3                4         Finance
# 9      104   Neha                2                1              HR
# 10     104   Neha                2                2              IT
# 11     104   Neha                2                4         Finance
