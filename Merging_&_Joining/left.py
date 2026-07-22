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

res=pd.merge(employees, departments, on="Department_ID", how="left")
print(res)
#    Emp_ID   Name  Department_ID Department_Name
# 0     101   Aman              1              HR
# 1     102   Riya              2              IT
# 2     103  Karan              3             NaN
# 3     104   Neha              2              IT
