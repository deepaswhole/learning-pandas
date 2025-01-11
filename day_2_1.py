import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'NY', 'Chicago']
})

#filtered_df = df[df['Age'] > 30]
#print(filtered_df)

#ny_df = df[df['City'] == 'NY']
#print(ny_df)

data = pd.DataFrame({
    'Country': ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil'],
    'Population': [1444216107, 1393409038, 331002651, 273523615, 220892340, 212559417],
    'Continent': ['Asia', 'Asia', 'North America', 'Asia', 'Asia', 'South America']
})
#pop_grtr_50 = data[(data['Population'] > 50) & (data['Continent'] == 'Asia')]
#print(pop_grtr_50)

#print(data['Country'].isin(['USA','Brazil'])) #the result is boolean
#print(data['Population'].between(144421600,1393409000))
#print(data['Continent'].str.contains('A', case=False))
#data_filltered = (data[data['Continent'].str.contains('A', case=False)])
#print(data_filltered)

#print(data.isnull) # check if any row is with missing value, eg Nan / False
#data_dropped = data.dropna() #drop the row with atleast 1 missing value, excluding imcomplete data from further analysis

data2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 35, None],
    'City': ['NY', 'LA', None, 'Chicago']
})

data2_filled = data2.fillna({
    'Age' : data2['Age'].mean(),
    'City' : 'Unknown'
})

print(data2_filled)
