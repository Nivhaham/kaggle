import pandas as pd


def main():
    ramen_df = pd.read_csv('ramen-ratings.csv')
    print(ramen_df)


if __name__ == '__main__':
    main()