

# Load libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

###
col_names_thyroid = ['Age', 'Gender', 'Smoking', 'Hx Smoking', 'Hx Radiothreapy', 'Thyroid Function', 
                     'Physical Examination', 'Adenopathy', 'Pathology', 'Focality', 'Risk', 'T', 'N', 'M', 
                     'Stage', 'Response', 'Recurred']
###

pima = pd.read_csv("diabetes.csv", header=None, names=col_names)

###
thyroid = pd.read_csv("Thyroid_Diff.csv", header=None, names=col_names_thyroid) ## whole file
###

print(thyroid['Age'])

print(pima.head())

###
print(thyroid.head())
###

feature_cols = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = pima[feature_cols] # Features
y = pima.label # Target variable

###
feature_cols_thyroid = ['Age', 'Gender', 'Smoking', 'Hx Smoking', 'Hx Radiothreapy', 'Thyroid Function', 
                         'Physical Examination', 'Adenopathy', 'Pathology', 'Focality', 'Risk', 'T', 'N', 'M', 
                         'Stage', 'Response']
X_thyroid = thyroid[feature_cols_thyroid]
y_thyroid = thyroid.Recurred
###

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

###
X_train_thyroid, X_test_thyroid, y_train_thyroid, y_test_thyroid = train_test_split(X_thyroid, y_thyroid, test_size=0.3, random_state=1)
###

clf = DecisionTreeClassifier(criterion='entropy')

###
clf_thyroid = DecisionTreeClassifier(criterion='entropy')
###

clf = clf.fit(X_train,y_train)

###
clf_thyroid = clf_thyroid.fit(X_train_thyroid, y_train_thyroid)
###

# print("Testing:")
# print(X_test.head())
# y_pred = clf.predict(X_test)
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

###
print("Testing:")
print(X_test_thyroid.head())
y_pred_thyroid = clf_thyroid.predict(X_test_thyroid)
print("Accuracy:", metrics.accuracy_score(y_test_thyroid, y_pred_thyroid))
###

print("\nEnter information for a new patient to predict whether they have diabetes or not:")

pregnant = int(input("How many times have you got pregnant: "))
insulin = float(input("Insulin level: "))
bmi = float(input("BMI: "))
age = int(input("Age: "))
glucose = float(input("Glucose level: "))
bp = float(input("Blood pressure: "))
pedigree = float(input("Pedigree function: "))

new_patient_data = pd.DataFrame([[pregnant, insulin, bmi, age, glucose, bp, pedigree]],
                                 columns=feature_cols)

prediction = clf.predict(new_patient_data)

if prediction[0] == 1:
    print("\nThe model predicts that the patient has diabetes.")
else:
    print("\nThe model predicts that the patient does not have diabetes.")

plt.figure(figsize=(15,8))
tree.plot_tree(clf, filled=True, rounded=True, max_depth=3, fontsize=10, feature_names=feature_cols,class_names=['0','1'])
plt.title("Decision tree trained on all features")
plt.show()