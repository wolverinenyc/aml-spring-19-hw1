import pandas as pd
from task1_3 import get_data

def test_shape():
    df = get_data('input.txt')
    assert df.shape[0]==225
    assert df.shape[1]==31

    # assert world population in 2010 is 7065 million

def test_pop2010():
    df = get_data('input.txt')
    assert int(df['2010'].sum()) == 7065
    print('Passed World Pop 2010')
