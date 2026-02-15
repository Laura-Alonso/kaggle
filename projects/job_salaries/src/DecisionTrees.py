#split dataset in features and target variable
x = data_DE_reg_salary.iloc[:, 1:5] # Features
y = data_DE_reg_salary.iloc[:, [0]] # Target variable

# Split dataset into training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) # 70% training and 30% test

# Pre-process data
import category_encoders as ce

encoder = ce.OrdinalEncoder(cols=["experience_level", "company_continent_name",'company_size'])
x_train = encoder.fit_transform(x_train)
x_test = encoder.transform(x_test)

# Fit the model and evaluate
clf_en = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
clf_en.fit(x_train, y_train)
y_pred_en = clf_en.predict(x_test)

from sklearn.metrics import accuracy_score
print('Model accuracy score with criterion entropy: {0:0.4f}'. format(accuracy_score(y_test, y_pred_en)))
y_pred_train_en = clf_en.predict(x_train)
y_pred_train_en
plt.figure(figsize=(12,8))
from sklearn import tree
tree.plot_tree(clf_en.fit(x_train, y_train))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred_en)
print('Confusion matrix\n\n', cm)