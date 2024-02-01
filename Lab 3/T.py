

# Load libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

col_names_thyroid = ['Age', 'Gender', 'Smoking', 'Hx Smoking', 'Hx Radiothreapy', 'Thyroid Function', 
                     'Physical Examination', 'Adenopathy', 'Pathology', 'Focality', 'Risk', 'T', 'N', 'M', 
                     'Stage', 'Response', 'Recurred']


thyroid = pd.read_csv("Thyroid_Diff.csv", header=None, names=col_names_thyroid) ## whole file


thyroid['Gender'].replace({'F' : 0, 'M' : 1, }, inplace=True)
thyroid['Smoking'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)

thyroid['Hx Smoking'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Hx Radiothreapy'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Physical Examination'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Adenopathy'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Pathology'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Focality'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Risk'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['T'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['N'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['M'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Stage'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Response'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)
thyroid['Recurred'].replace({'No' : 0, 'Yes' : 1, }, inplace=True)

print(thyroid)
#print(thyroid.head())

feature_cols_thyroid = ['Age', 'Gender', 'Smoking', 'Hx Smoking', 'Hx Radiothreapy', 'Thyroid Function', 
                         'Physical Examination', 'Adenopathy', 'Pathology', 'Focality', 'Risk', 'T', 'N', 'M', 
                         'Stage', 'Response']
X_thyroid = thyroid[feature_cols_thyroid]
y_thyroid = thyroid.Recurred

X_train_thyroid, X_test_thyroid, y_train_thyroid, y_test_thyroid = train_test_split(X_thyroid, y_thyroid, test_size=0.3, random_state=1)

clf_thyroid = DecisionTreeClassifier(criterion='entropy')

clf_thyroid = clf_thyroid.fit(X_train_thyroid, y_train_thyroid)

print("Testing:")
print(X_test_thyroid.head())
y_pred_thyroid = clf_thyroid.predict(X_test_thyroid)
print("Accuracy:", metrics.accuracy_score(y_test_thyroid, y_pred_thyroid))

plt.figure(figsize=(15,8))
tree.plot_tree(clf, filled=True, rounded=True, max_depth=3, fontsize=10, feature_names=feature_cols_thyroid,class_names=['0','1'])
plt.title("Decision tree trained on all features")
plt.show()