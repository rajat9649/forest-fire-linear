import pandas as pd 
from pandas_profiling import ProfileReport

df=pd.read_csv('forestfires.csv')

pro=ProfileReport(df,title='pandas profiling report')
pro.to_file('forestfires.html')