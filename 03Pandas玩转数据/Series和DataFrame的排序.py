import numpy as np
import pandas as pd
from  pandas import Series,DataFrame

#Series的排序
s1 = Series(np.random.randn(10))
print(s1)
print(s1.index)
print(s1.values)
s2 = s1.sort_values(ascending=False)
print(s2)
s3 = s2.sort_index()
print(s3)

#DataFrame排序

df1 = DataFrame(np.random.randn(20).reshape(4,5),columns=["c1","c2","c3","c4","c5"])
print(df1)

df2 = df1.sort_values('c2',ascending=False)#按照C2列排序
print(df2)
df3 = df2.sort_index()#按照index排序
print(df3)


#作业

movie = pd.read_csv("movie_metadata.csv")
tmp = DataFrame([movie['director_name'],movie['imdb_score'],movie["movie_facebook_likes"]]).T.sort_values('imdb_score',ascending=False)
print(tmp)
tmp.to_csv("movie_sort.csv",index=False)
