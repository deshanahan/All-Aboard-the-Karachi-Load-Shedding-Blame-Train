import pandas as pd
import numpy as np
from KLS_Data import name_set_list, blamed_list, karachi_ls_df, kls_df

def name_set_length_lister(name_set_list):
    '''Returns a list of the lengths of a passed iterable.'''
    name_set_length_list = [len(name_set) for name_set in name_set_list]
    return name_set_length_list

kls_df.T.info()

blamed_percent = pd.DataFrame([kls_df.loc[blamed].value_counts(normalize = True) for blamed in kls_df.T])
blamed_percent.plot.bar()

# Find the length of the name_set_list
name_set_lengths = name_set_length_lister(name_set_list)

# Create a dictionary of the blamed entities and the number of times each entity is blamed
blamed_dict = dict(zip(blamed_list, name_set_lengths))
print(blamed_dict)

# Create a pandas Series out of the dictionary
times_blamed = pd.Series(blamed_dict)

new_search_percentage = pd.Series(times_blamed.values/len(karachi_ls_df.columns))
new_search_percentage

blamed_percent['new_search_percentage'] = new_search_percentage.values
blamed_percent = blamed_percent.drop(columns = 0)
blamed_percent.columns = ['Overall Percent', 'New Search Percent']
blamed_percent.plot.bar()

# Print the total and average of the times_blamed Series

blamed_num = pd.DataFrame([kls_df.loc[blamed].value_counts() for blamed in kls_df.T])

print(f'The total times all entities in the dataset have been blamed for load shedding in Karachi, Pakistan is {sum(blamed_num[1])}.')
print(f'The average number of times the entities in the dataset have been blamed for load shedding in Karachi, Pakistan is {np.mean(blamed_num[1])}.')

# Plot a histogram of the times_blamed Series
blamed_num[1].plot.hist()

# Drop a few rows of the times_blamed Series to make it more normalized
blamed_percent.drop(blamed_percent[blamed_percent['Overall Percent']< 0.25].index, inplace = True)
blamed_percent['Overall Percent'].plot.hist()

# Plot a bar chart for the times_blamed Series
blamed_percent['Overall Percent'].plot.bar(legend = False)

# Create a separate dataframe consisting of 10 random samples of the columns
sample_karachi_ls_df = karachi_ls_df.sample(n=10, axis=1)

# Find a count of all True values and all False values in the sample
unique_sample = np.unique(sample_karachi_ls_df, return_counts = True)
print(unique_sample)

# Create a dataframe out of the True/False numpy array
unique_sample_df = pd.DataFrame(unique_sample)

# Rename the columns after the first row
unique_sample_df.rename(columns=unique_sample_df.iloc[0], inplace = True)

# Remove the old first row
unique_sample_df.drop([0], inplace = True)

# Create a bar chart out of the False/True sample
ax = unique_sample_df.plot.bar(title = 'Who is Being Blamed for Load Shedding in Karachi: True/False Samples')
ax.set(xlabel = 'True/False', ylabel = 'Occurences in sample')

# Find who is being blamed the most
def who_is_to_blame(alist, df):
    '''Iterates over a list and prints the item in the list followed by
    unique counts in a numpy array.'''
    for b in alist:
        array = f'{b}:', np.unique(df.loc[b], return_counts = True)
        print(array)

who_is_to_blame(blamed_list, kls_df)

# Create a new dataframe with only the entities that we want
new_kls_df = kls_df.drop('Imran Khan').drop('Asad Umar').drop('Naeem Rehman').drop('Omar Ayub Khan')
new_kls_df

new_blamed_list = ['Karachi Electric', 'NEPRA', 'Sui Gas', 'Tehreeki Insaaf']

# Call who_is_to_blame function on the new list and dataframe
who_is_to_blame(new_blamed_list, new_kls_df)