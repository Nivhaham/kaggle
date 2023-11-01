import pandas as pd


def main():
    df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
                       'Sue': ['Pretty good.', 'Bland.']},
                      index=['Product A', 'Product B'])

    pd.Series([30, 35, 40], index=['2021 Sales', '2022 Sales', '2023 Sales'], name='Ice Cream')

    # Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second
    print(df['Bob'][0])
    print(df.iloc[1][0])
    print(df.iloc[:, 0])


if __name__ == '__main__':
    main()
