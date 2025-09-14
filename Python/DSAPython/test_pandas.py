import pandas as pd
# print(pd.__version__)
df = pd.DataFrame({'Bank client ID': [1, 2, 3, 4],
                   'Year of birth': [1980, 1996, 1970, 1985],
                   'Account balance': [1000.50, 1500.75, 2000.00, 2500.25]})
# print(df)
# # print(np.__version__)   
pd1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
pd2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
# print(pd1)

data = [[1,'article',100],
        [2,'book',200],
        [3,'magazine',150]]

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data, index=['ID', 'Type', 'Price'], columns=['First', 'Second', 'Third'])

df1.columns = ['Student_ID', 'Student_Name', 'Exam_Score']
df1 = df1.set_index('Student_ID', drop=False)
print(df1)