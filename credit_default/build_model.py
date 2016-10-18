# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.datasets import load_iris
# from sklearn.externals import joblib

import pandas as pd
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


# if __name__ == "__main__":
#         # Load Iris Data
#         iris_data = load_iris()
#         features = iris_data.data
#         feature_names = iris_data.feature_names
#         target = iris_data.target
#         target_names = iris_data.target_names
#
#         knn = KNeighborsClassifier(n_neighbors=3)  # replace with your own ML model here
#         knn.fit(features, target)
#
#         joblib.dump(knn, 'models/iris_model.pkl')
if __name__ == "__main__":
    #load data
    df = pd.read_csv('default_of_credit_card_clients.csv')
    df = df.dropna()
    df = df.drop('ID', axis = 1)
    features = df.iloc[:, :5]
    feature_names = list(features.columns.values)
    target = df['default payment next month']
    # target= target.replace(to_replace=0, value="Paid")
    # target= target.replace(to_replace=1, value="Default")
    target_names = ["Paid", "Default"]

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(features, target)
    joblib.dump(knn, 'models/credit_model.pkl')
