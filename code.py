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

#Mapping the grade feature 
map1={'O':10,'A+':9,'A':8,'B+':7,'B':6,'C':5,'D':4,'E':3,'F':2}
features['Grade']=features['Grade'].map(map1)
print(features['Grade'])

#Label Encoder
#the word labels are converted into number Label
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
features['Course']=le.fit_transform(features['Course'])
features['MHRDName']=le.fit_transform(features['MHRDName'])
features['ScholarType']=le.fit_transform(features['ScholarType'])
features['Direction']=le.fit_transform(features['Direction'])
features['Gender']=le.fit_transform(features['Gender'])
features['Medium']=le.fit_transform(features['Medium'])
features['CourseType']=le.fit_transform(features['CourseType'])
features['ProgramType']=le.fit_transform(features['ProgramType'])
