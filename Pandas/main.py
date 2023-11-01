import pandas as pd


def main():
    ramen_df = pd.read_csv('ramen-ratings.csv')
    print(ramen_df)
    print(ramen_df.Stars.describe())
    # line 9, 10 same
    #print(ramen_df.Stars.unique())
    #print(ramen_df['Stars'].unique())


if __name__ == '__main__':
    main()