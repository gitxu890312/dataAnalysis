import numpy as np
import pandas as pd
# from pandas import Series,DataFrame

df1 = pd.read_csv('movie_metadata.csv')
# print(df1)
print(df1.columns)
print(df1.shape)

print(df1.head())
print(df1.tail())

print(df1[['director_name','aspect_ratio']])

sub_df = df1[['director_name', 'movie_title','imdb_score','budget', 'title_year']]
print(sub_df.tail())
print(sub_df.head())

#根据索引截取dataFrame iloc
tmpdf = sub_df.iloc[10:20,0:3]
print(tmpdf)
tmpdf = tmpdf.iloc[2:4,0:3]
print(tmpdf)


#根据label截取dataFrame
tmpdf = sub_df.loc[15:17,"director_name":"budget"]
print(tmpdf)