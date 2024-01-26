import pandas as pd 
# indexing deries
"""mydataset=["physics klb","kiswahili", "mathematics kmf"]
myvar=pd.Series(mydataset,index=['A','B','C'])
print(myvar)
print(myvar["C"])"""

# series from dic.
"""mydatasets={"MON":23, "TUE":19, "WED":20, "THUR":19, "FRI":21,"SAT":19, "SUN":22

}
myvar=pd.Series(mydatasets)
myvar=pd.Series(mydatasets, index=["MON","FRI"])
print(myvar)"""

# DataFrames
""" data={
    'Intake':["JAN", "MAY", "SEP"],
'students':[12300,10234,15343] 
}
df=pd.DataFrame(data,index=["A","B","C"])
print(df)
print(df.loc["A"])""""
dt=pd.read_csv("Central Bank Rate (CBR) ")
print(dt)







