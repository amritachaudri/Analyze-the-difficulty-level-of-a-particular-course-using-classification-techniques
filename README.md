# Analyze-the-difficulty-level-of-a-particular-course-using-classification-techniques
The dataset contains the information of the students in bachelor of Technology in biotechnology
The data set has 22 columns and 6 rows. In this project we are trying to analyse the difficulty level of a particular course that is biotechnology
## Step by Step approach for creating the Model
### Step 1: Import Dataset
The data set containing the information about the students is imported.

### Step 2: Data Pre-Processing
In this step we are trying to perform feature scaling on the given data set. First we perform mapping on feature 'Grade'. Then we perform label encoding on the given data set as it convert is the categorical data into numerical data. Then with the help of ” imputer ”we remove null values present in the data set as we cannot remove the column of the row containing the null values the strategy used for removing the null values is mean

### Step 3:Visualization
In this step we plot graph between different features of the data set such as grade, course attendance, different evaluations, and with the help of heat map check the relationship different features of the data set.
 
### Step 4:Splitting the data set
With the help of train test split, we split the data set into parts that is training and testing.

### Step 5: Training the model
We choose some models for the comparative study. The models chosen are SVM, linear regression k nearest neighbours, naive Bayes.

### Step 6:Hyper parameter tuning: 
With the use of pipeline we perform hyper parameter tuning on linear regression classification model. 
### Step 7: Confusion matrix: 
With Help of confusion matrix on SVM we try to visualise the classified data.

### Step 8:Checking the accuracy: 
Check the accuracy of the above models by R2 score as the models are classification models

### Step 9:Checking the difficulty level of the course: 
The Result mean grade of all the students available in the data set ,if the mean is between 0 to 30 percentage the course is referred as difficult else if the range between 40 to 70 percent then the course is referred as medium else if the percentage is above 70 the course is referred as easy. 
