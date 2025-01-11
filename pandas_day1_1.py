import pandas as pd
import numpy as np

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35],
    'City' : ['New York', 'Paris', 'London']
}

students = [
    ['John', 88, 90],
    ['Mia', 92, 85],
    ['Leo', 92, 85],
    ['Sara', 85, 92]
]

#df_no_index = pd.DataFrame(students)
#df_list = pd.DataFrame(students, columns=['Name', 'Math Score','English Score'])
#print(df_no_index)
#print(df_list)

arr = np.array([
    [101, 102, 103],
    [40, 45, 50]
])

#df_arr = pd.DataFrame(arr, index=['Height (cm)', 'Weight (kg'], columns=['Student A', 'Student B', 'Student C'])
#print(df_arr)

#df = pd.DataFrame(data)
#df.to_csv('data.csv', index=False)

#df2 = pd.read_csv('data.csv')
#print(df2.head())

#std = pd.DataFrame(students)
#std = pd.DataFrame(students, columns=['Name', 'Math Score', 'English Score'])
#std.to_csv('students.csv', index=False)

#std2 = pd.read_csv('students.csv')
#print(std2)

Learners = [
    ['Alice','25','89'],
    ['Bob','22','76'],
    ['Carol','23','92'],
    ['Dave','24','85'],
    ['Eve','21','95'],
    ['Frank','27','80'],
    ['Grace','26','88'],
    ['Helen','25','77'],
    ['Issac','23','90'],
    ['Astra','17','93']
]

#Lnr = pd.DataFrame(Learners, columns= ['Name', 'Age', 'Score'])
#Lnr.to_csv('learner.csv', index=False)
#
#lnr = pd.read_csv('learner.csv')
#print(lnr.head())
#print(lnr.head(7))
#print(lnr.tail(3))
#print(lnr.describe())

#lnr = pd.DataFrame(Learners, columns= ['Name', 'Age', 'Score'])
#lnr.to_excel('learner.xlsx', index=False)

#lnr2 = pd.read_excel('learner.xlsx')
#print(lnr2)

lnr = pd.DataFrame(Learners, columns=['Name', 'Age', 'Score'])
lnr.to_json('learner.json')
lnr2 = pd.read_json('learner.json')
#print(lnr2)
#print(lnr2.shape)
#print(lnr.info())
#print(lnr.columns)
#print(lnr.dtypes)

participants = [
    ['Jason', '25', '190'],
    ['Peter', '21', '181'],
    ['Ray', '24', '184']
]

#ptn_no_index = pd.DataFrame(participants)
#print(ptn_no_index)
ptn = pd.DataFrame(participants, columns=('Participant', 'Age', 'Height'))
ptn.to_csv('participants.csv', index=False)
ptnr = pd.read_csv('participants.csv')
#print(ptnr)

dt3 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

#print(dt3['A'])
#print(dt3[['A', 'C']])
#print(dt3[['A', 'B' ,'C']])

#print(dt3.loc[0])
#print(dt3.iloc[2])

data2 = {'A' : [10,20,30], 'B' : [40, 50, 60]}
df4 = pd.DataFrame(data2, index=[1,2,3])

#print(f"DataFrame:\n{df4}")

print(f" Using loc to locate row with index 1 : \n{df4.loc[1]}")
print(f" Using iloc to locate row with exact position : \n{df4.iloc[2]}")