from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC


class StructuralPatternName:
    def __init__(self, *args) -> None:
        self.classificators = list(args)


    def fit(self, X, y):
        for c in self.classificators:
            c.fit(X, y)


    def predict(self, X, y):
        minv = 1
        result = None
        for c in self.classificators:
            predicted = c.predict(X)
            v = metrics.accuracy_score(y, predicted)
            if v < minv:
                minv = v
                result = c
        return result, v


if __name__ == "__main__":
    X, y = datasets.load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    svm_l = svm.SVC(kernel='linear')
    svm_r = svm.SVC(kernel='rbf')
    # svm_p = svm.SVC(kernel='polynomial')
    lsvc = LinearSVC(random_state=0, tol=1e-5)

    patterns = StructuralPatternName(svm_l, svm_r, lsvc)
    patterns.fit(X_train, y_train)
    clf, accuracy = patterns.predict(X_test, y_test)
    print(f"Classificatory : {clf} , Accuracy: {accuracy}")
