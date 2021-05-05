import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

dataset = np.insert(iris.data, 0, iris.target,axis=1)
x
df = pd.DataFrame(data=dataset, columns=["iris_id"] + iris.feature_names)
X = df.iloc[:,1:]
y = df.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

train_df = X_train.copy()
train_df.insert(0, "iris_id", y_train)
train_df.to_csv("input/data/train/training.csv", sep=",", header=None, index=None)

test_df = X_test.copy()
test_df.insert(0, "iris_id", y_test)
test_df.to_csv("input/data/validation/testing.csv", sep=",", header=None, index=None)
