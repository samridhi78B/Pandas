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

res=pd.merge(employees, departments, on="Department_ID", how="outer")
print(res)
#    Emp_ID   Name  Department_ID Department_Name
# 0   101.0   Aman              1              HR
# 1   102.0   Riya              2              IT
# 2   104.0   Neha              2              IT
# 3   103.0  Karan              3             NaN
# 4     NaN    NaN              4         Finance
