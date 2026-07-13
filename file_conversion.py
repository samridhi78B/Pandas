import pandas as pd
data ={
    "Name" : ['Avni', 'Sam', 'Kanika'],
    "Age" : [13,20,24],
    "City" : ['Jalandhar', 'Ludhiana','Amritsar']
}

df=pd.DataFrame(data)
print(df)
#output
#    Name  Age       City
# 0    Avni   13  Jalandhar
# 1     Sam   20   Ludhiana
# 2  Kanika   24   Amritsar

# df.to_json("output.json", index=False) #creates json file with name output.json 
# df.to_excel("output.xlsx", index=False)
# df.to_csv("output.csv", index=False)

#index=false-> this will not add 0,1,2  in files
