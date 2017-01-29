import pandas as pd


def replace_column_values(df, dict, col_name, new_col_name=None):
    df_return = df.copy()
    if new_col_name is None:
        df_return[col_name].replace(dict, inplace=True)
    else:
        df_return[new_col_name] = df_return[col_name].replace(dict, inplace=False)
    return df_return


def get_unique_values_in_column(df, col_name):
    return df[col_name].unique()


def get_random_fraction_of_rows(df, row_fraction=0.5):
    return df.sample(frac=row_fraction)


def get_random_number_of_rows(df, num_rows):
    return df.sample(n=num_rows)


def select_rows_by_position(df, row_ini, row_end):
    return df.loc[row_ini:row_end]

def select_value_by_position(df, vector_row_pos, vector_col_pos):
    return df.iloc[vector_row_pos, vector_col_pos]


if __name__ == "__main__":

    df = pd.DataFrame({'letters':['a','a','c'],
                       'numbers':[1,2,3]})
    print(df)

    print("Example of replacing values:")
    dict = {'a':1}
    df_return = replace_column_values(df, dict, 'letters')
    print(df_return)                                                                                                                                                                                                                                                                                                          

    print("Example of replacing values in a new column")
    df_return = replace_column_values(df, dict, 'letters', 'new_column')
    print(df_return)

    print("Example of getting unique values")
    df_unique = get_unique_values_in_column(df, 'letters')
    print(df_unique)

    df_sample = get_random_fraction_of_rows(df, 0.6)
    print(df_sample)

    df_num = get_random_number_of_rows(df, 1)
    print(df_num)

    df_rows_pos = select_rows_by_position(df, 0, 1)
    print(df_rows_pos)

    value = select_value_by_position(df, vector_row_pos=[0,2], vector_col_pos=[0,1])
    print(value)



