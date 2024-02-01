
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
thyroid['Thyroid Function'].replace({'Clinical Hyperthyroidism' : 0, 'Clinical Hypothyroidism' : 1,'Euthyroid' : 2, 'Subclinical Hyperthyroidism' : 3, 'Subclinical Hypothyroidism' : 4 }, inplace=True)
thyroid['Physical Examination'].replace({'Normal' : 0, 'Single nodular goiter-left' : 1,'Single nodular goiter-left' : 2, 'Single nodular goiter-right' : 3, 'Multinodular goiter' : 4, 'Diffuse goiter' : 5 }, inplace=True)
thyroid['Adenopathy'].replace({'Bilateral' : 0, 'Extensive' : 1, 'Left' : 2, 'No' : 3, 'Posterior' : 4, 'Right': 5 }, inplace=True)
thyroid['Pathology'].replace({'Follicular' : 0, 'Hurthel cell' : 1, 'Micropapillary' : 2, 'Papillary' : 3 }, inplace=True)
thyroid['Focality'].replace({'Multi-Focal' : 0, 'Uni-Focal' : 1, }, inplace=True)
thyroid['Risk'].replace({'High' : 0, 'Intermediate' : 1, 'Low' : 2, }, inplace=True)
thyroid['T'].replace({'T1a' : 0, 'T1b' : 1, 'T2' : 2, 'T3a' : 3, 'T3b' : 4, 'T4a' : 5, 'T4b' : 6}, inplace=True)
thyroid['N'].replace({'N0' : 0, 'N1a' : 1, 'N1b' : 2}, inplace=True)
thyroid['M'].replace({'M0' : 0, 'M1' : 1, }, inplace=True)
thyroid['Stage'].replace({'I' : 0, 'II' : 1, 'I' : 2, 'III' : 3, 'IVA' : 4, 'IVB' : 5,}, inplace=True)
thyroid['Response'].replace({'Biochemical Incomplete' : 0, 'Excellent' : 1, 'Indeterminate' : 2, 'Structural Incomplete' : 3, }, inplace=True)
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
tree.plot_tree(clf_thyroid, filled=True, rounded=True, max_depth=3, fontsize=10, feature_names=feature_cols_thyroid,class_names=['0','1'])
plt.title("Decision tree trained on all features")
plt.show()