import os
import glob
import pandas as pd


home_data_path  = os.path.expanduser('~')
data_file = os.path.join(home_data_path,'WH-project','WH-analysis','WH_data_train.csv')
print(data_file)


def getYearlyData(path_to_WH_data:str,year:int):
    df = pd.read_csv(path_to_WH_data)
    red_df = df.loc[df["Year"]==year,["Life Ladder","Log GDP per capita","Social support","Healthy life expectancy at birth","Freedom to make life choices"]]
    return red_df


