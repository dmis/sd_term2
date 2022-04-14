from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


class CreationalPatternName:
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def get_subsample(self, df_share):
        if df_share >= 100:
            return self.X_train, self.y_train
        X_train, X_test, y_train, y_test = train_test_split(self.X_train, self.y_train,
                                                            train_size=df_share / 100,
                                                            random_state=42)
        return X_train, y_train


if __name__ == "__main__":
    X, y = datasets.load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        train_size=0.67,
                                                        random_state=42)

    pattern_item = CreationalPatternName(X_train, y_train)
    for df_share in range(10, 101, 10):
        curr_X_train, curr_y_train = pattern_item.get_subsample(df_share)

        regression = linear_model.LinearRegression()
        regression.fit(curr_X_train, curr_y_train)

        y_pred = regression.predict(X_test)

        print("df_share: ", df_share)
        print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
