import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

data = pd.read_csv("data.csv")
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0).
