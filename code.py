#import the dataset that contains the data of the students in biotechnogoly
import pandas as pd
df=pd.read_csv(r'C:\Users\Harprem Singh Chaudr\Documents\btech_data.csv')
print(df.head(5))
#Understanding the dataset
print("Checking the size of the file")
print(df.size)
print("The number of rows are")
print(df.shape[0])
print("The number of columns are")
print(df.shape[1])
print("Viewing the detailed data")
print(df.describe())
features=df.columns[:22]
print(features)
features=df[features]
