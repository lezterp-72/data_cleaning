#RUN AS: python -m pytest test_df.py   
import pytest
import pandas as pd
#put your file name here (the cleaned up version)
df = pd.read_csv('alumni_clean.csv', index_col='Id')

#The tests that you crowd-sourced are below.
def test_eliminations():
    assert 9229 not in df.index
    assert 9211 not in df.index
    assert 2669 not in df.index
    assert 10538 not in df.index

def test_birthday_cleaning():
    #assert df.loc[12331, "Birth_Year"] == 1965
    assert df.loc[586, "Birth_Year"] == 1912
    assert df.loc[2881, "Birth_Year"] == 1930
    assert df.loc[6140, "Birth_Year"]== 1902
    assert df.loc[1182, "Birth_Year"]== 1910
    assert df.loc[5769, "Birth_Year"]== 1873

#my file didn't pass this one - I would save this for last
#Shouldn't pass. Was 24 at Graduation
def test_hard_cases():
    assert df.loc[8524, "Birth_Year"] == 1947

def test_exit_cleaning():
    assert df.loc[11283, "Exit_Year"] == 1961
    assert df.loc[5037, "Exit_Year"] == 1978
    assert df.loc[630, "Exit_Year"] == 1964
    assert df.loc[10073, "Exit_Year"] == 1898
    assert df.loc[28, "Exit_Year"] == 1929
    assert df.loc[4316, "Exit_Year"] == 1957

def test_filtering_exits():
    for elm in df["Exit_Year"]:
        assert elm >= 1880
        assert elm <= 1984

def test_filtering_bday():
    for elm in df["Birth_Year"]:
        assert elm >= 1857
        assert elm <= 1980




