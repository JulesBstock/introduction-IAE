import pandas as pd
import numpy as np

col1 = [i for i in range(4)]
col2 = [float(i**2) for i in range(4)]
col3 = ['cat1', 'cat2', 'cat3', 'cat1']
print(col1)

MyDataframe = pd.DataFrame({'INDEX': col1,
                            'DATE': pd.Timestamp('20130102'),
                            'SQUARED': col2,
                            'THREE': np.array([3]*4, dtype='int32'),
                            'SET': pd.Categorical(["test", "train", "test", "train"]),
                            'CAT': col3})

# print entire data frame
print(MyDataframe)

# print only first 2 rows
print(MyDataframe.head(2))

# print last 3 rows
print(MyDataframe.tail(3))

# print the datatypes of the columns
print(MyDataframe.dtypes)

# print columnames
print(MyDataframe.columns)

# print the index
print(MyDataframe.index)

# give a summary of the dataframe
print(MyDataframe.describe)

print(MyDataframe[MyDataframe['SET'] == 'test'])

MyDataframe.pop('THREE')
MyDataframe = MyDataframe.drop('CAT',  axis=1)
print(MyDataframe)

def addset(string):
    return string + ' set'
MyDataframe['SET'] = MyDataframe['SET'].map(addset)
print(MyDataframe)

MyDataframe['SET'] = MyDataframe['SET'].map(lambda x: x.upper())
print(MyDataframe)

MyDataframe2 = pd.DataFrame({'INDEX':[2,3,1,0], 'VALUE2':[11,22,33,44]})
# other options for how are 'inner', 'outer', 'right'
print(MyDataframe2)

MyDataframe3 = pd.merge(MyDataframe, MyDataframe2, how='left', on='INDEX')
print(MyDataframe3)

