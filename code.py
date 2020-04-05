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
print("Features after Label Encoding")
print(features.head(5))


print("Checking the null values present in the dataset")
print(features.isnull().sum())
print("Eliminating the null values")
import numpy as np
from sklearn.preprocessing import Imputer
im=Imputer(strategy='mean',missing_values=np.nan)
features['MTT_50']=im.fit_transform(features[['MTT_50']].values)
features['ETT_100']=im.fit_transform(features[['ETT_100']].values)
features['ETP_100']=im.fit_transform(features[['ETP_100']].values)
features['Course_Att']=im.fit_transform(features[['Course_Att']].values)
print(features.isnull().sum())

#visualizing the data
import matplotlib.pyplot as plt
features.plot.bar(x = 'Regd No', y = 'Grade')
features.plot.bar(x = 'Regd No', y = ['MTT_50','ETT_100','ETP_100','CA_100'])
features.plot.bar(x = 'Regd No', y = 'Course_Att')

#Plotting heatmap
#To find the relationship between marks,attendence and grades
df1=features[['MTT_50','ETT_100','ETP_100','CA_100','Grade']]
print(df1.head(4))
import seaborn as sns
hm=pd.pivot_table(df1,values='Grade',index=['ETT_100'],columns='CA_100')
sns.heatmap(hm)

#Applying StandardScaler
#to arrange the data in a normal distribution
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
data1=sc.fit_transform(features)

#Splitting the dataset into testing and training set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(y,grade,test_size=0.3,random_state=0)
print("Training and testing split was successful.")

#Appling Pipeline 
#for fitting and transforming the classifiers
from sklearn.pipeline import Pipeline
#Checking different classification method to select the best classifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
#importing accuracy score of the classifier
from sklearn.metrics import r2_score
#Using the pipeline
pipe=Pipeline([('sls',StandardScaler()),('logistic Reg',LogisticRegression(random_state=2)) ])
pipe.fit(X_train,y_train)
x_p=pipe.predict(X_test)
print(r2_score(x_p,y_test))
svm=SVC(kernel='linear')
svm.fit(X_train,y_train)
x_s=svm.predict(X_test)
print(r2_score(x_s,y_test)*100)

#Checking the confusion matrix for SVM
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,x_s)
print(cm)

nv=GaussianNB()
nv.fit(X_train,y_train)
x_n=nv.predict(X_test)
print("The accuracy of Naive bayes classifiers:")
print(r2_score(x_n,y_test)*100)
de=DecisionTreeClassifier(criterion='gini')
de.fit(X_train,y_train)
x_d=de.predict(X_test)
print("The accuracy of DecisionTreeClassifier classifiers:")
print(r2_score(x_d,y_test)*100)
knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train,y_train)
x_k=knn.predict(X_test)
print("The accuracy of KNeighborsClassifier classifiers:")
print(r2_score(x_k,y_test)*100)
