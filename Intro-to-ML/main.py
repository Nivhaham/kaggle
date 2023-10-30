import os
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def validating_model(X, y):
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
    # Define model
    melbourne_model = DecisionTreeRegressor()
    # Fit model
    melbourne_model.fit(train_X, train_y)

    # get predicted prices on validation data
    val_predictions = melbourne_model.predict(val_X)
    print(mean_absolute_error(val_y, val_predictions))

    # Forest model

    forest_model = RandomForestRegressor(random_state=1)
    forest_model.fit(train_X, train_y)
    melb_preds = forest_model.predict(val_X)
    print(mean_absolute_error(val_y, melb_preds))


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

    # print("The predictions are")
    # print(melbourne_model.predict(X.head()))
    validating_model(X, y)


if __name__ == '__main__':
    main()
