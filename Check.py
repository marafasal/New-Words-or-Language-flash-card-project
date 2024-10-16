import pandas as pd

df=pd.read_csv("data/french_words.csv")
dflist=df['French']
dflist2=[]
for item in dflist:
    if item=="histoire" or item=="ville" or item=="eux":
        dflist.drop(item)
        dflist2.append(item)
print(dflist2)



#
# list1=[1,2,3,4,5]
# list2=[]


# for item in df:
#     if df==3:
#         list1.remove(item)
#
#         list2.append(item)
#
#         df.to_csv("to_learn.csv")
#
#
# print(list2)
