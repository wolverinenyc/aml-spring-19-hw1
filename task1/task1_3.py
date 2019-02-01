import pandas as pd

def get_data(x):
    df = pd.read_csv(x, encoding='UTF-16', error_bad_lines=False,
                 escapechar='\\',index_col=0)

    # obtain world population in 2010: need to convert characters to string
    cols = df.columns
    df[cols] = df[cols].apply(pd.to_numeric,errors='coerce')
    return df
