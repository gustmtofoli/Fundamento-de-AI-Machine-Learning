# LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
print(">>> [OK] Logistic Regression")

# NEURAL NETWORK
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier()
print(">>> [OK] Neural Network")

# DECISION TREES
from sklearn.ensemble import GradientBoostingClassifier
classifier = GradientBoostingClassifier()
print(">>> [OK] Decision Trees")

# SVM
from sklearn.svm import SVC
classifier = SVC()
print(">>> [OK] Support Vector Machine")
