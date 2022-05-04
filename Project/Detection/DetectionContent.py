# -*- coding: UTF-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


class Detection(object):

    def __init__(self):
        self.label = None
        self.data = None
        self.clf = None
        self.models_name = {
            "knn": KNeighborsClassifier(n_neighbors=6),
            "naive_bayes": GaussianNB(),
            "logit": linear_model.LogisticRegression(solver="lbfgs", multi_class="auto"),
            # "ridge": linear_model.BayesianRidge(),
            "svm": SVC(kernel="rbf", gamma="auto"),
            "decision_tree": DecisionTreeClassifier(),
            "random_forest": RandomForestClassifier(n_estimators=100),
            "mlp": MLPClassifier(solver="adam", alpha=1e-01, hidden_layer_sizes=(2,), random_state=1),
            "sgd": SGDClassifier(loss="hinge", penalty="l2"),
            # "knr": KNeighborsRegressor(5)
        }

    def load_data(self, data):
        self.data = data

    def detect(self, model_name):
        self.clf = self.models_name[model_name]
        self.clf.fit(self.data["train_data"], self.data["test_data"])
        predictions = self.clf.predict(self.data["test_data"])
        res = f1_score(self.data["test_label"], predictions)
        return res
