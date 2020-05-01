import pandas as pd
#Import Library Pandas
myFile = "./Tcp"
df = pd.read_csv(myFile) 
df["Length"] = pd.to_numeric(df["Length"])
df.insert(7,'Outcome','no')
df.to_csv(myFile)
print(df.head(3))
