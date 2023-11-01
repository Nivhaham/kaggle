import pandas as pd


def main():
    ramen_df = pd.read_csv('ramen-ratings.csv')
    print(ramen_df)
    print(ramen_df.Stars.describe())
    # line 9, 10 same
    #print(ramen_df.Stars.unique())
    #print(ramen_df['Stars'].unique())

    #apply() is a built in method in pandas used for changing a whole column

    print(ramen_df.Stars.value_counts())
    print(ramen_df.groupby('Stars').Stars.count())

    ramen_df_sorted_by_brand_name = ramen_df.reset_index()
    ramen_df_sorted_by_brand_name.sort_values(by=['Brand'], ascending=True)
    print(ramen_df_sorted_by_brand_name)

if __name__ == '__main__':
    main()