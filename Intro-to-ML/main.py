import os
import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def main():
    melbourne_data = pd.read_csv("melb_data.csv")
    # print(melbourne_data.describe())
    # print(melbourne_data.columns)

    melbourne_data = melbourne_data.dropna(axis=0)
    y = melbourne_data.Price
    # print(y)

    # Picking Subset of Columns
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = melbourne_data[melbourne_features]
    print(X.describe())

    melbourne_model = DecisionTreeRegressor(random_state=1)

    # Fit model
    melbourne_model.fit(X, y)

    print("Making predictions for the following 5 houses:")
    print(X.head())
    print("The predictions are")
    print(melbourne_model.predict(X.head()))


if __name__ == '__main__':
    main()
