# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:31:04 2018

@author: CJ O'Sullivan
"""

# Importing data analysis packages.
import pandas
import numpy

# Importing nesarc csv file.
add_health_data = pandas.read_csv('addhealth_pds.csv', low_memory=False)

## Used to avoid runtime errors.
pandas.set_option('display.float_format',lambda x:'%f'%x)



## ## ## ## ## ---- Inital AddHealth Dataset Analysis ---- ## ## ## ## ##
# Number of observations or rows in the dataset. 
print('Number of rows in the AddHealth dataset.')
print(len(add_health_data))

# Number of varianles or columns in the dataset.
print('Number of columns in the AddHealth dataset.')
print(len(add_health_data.columns))

## ## ## ## ## ---- Determining the childrens ethnicity.  ---- ## ## ## ## ##

# Making sure all ethnicity data is numeric.
add_health_data['H1GI4']=pandas.to_numeric(add_health_data['H1GI4'])
add_health_data['H1GI6A']=pandas.to_numeric(add_health_data['H1GI6A'])
add_health_data['H1GI6B']=pandas.to_numeric(add_health_data['H1GI6B'])
add_health_data['H1GI6C']=pandas.to_numeric(add_health_data['H1GI6C'])
add_health_data['H1GI6D']=pandas.to_numeric(add_health_data['H1GI6D'])

# Removing unused values - 6 = refused, 8 = don't know.
add_health_data['H1GI4'] = add_health_data['H1GI4'].replace([6,8],numpy.nan)
add_health_data['H1GI6A'] = add_health_data['H1GI6A'].replace([6,8],numpy.nan)
add_health_data['H1GI6B'] = add_health_data['H1GI6B'].replace([6,8],numpy.nan)
add_health_data['H1GI6C'] = add_health_data['H1GI6C'].replace([6,8],numpy.nan)
add_health_data['H1GI6D'] = add_health_data['H1GI6D'].replace([6,8],numpy.nan)

# Suming each of the variables and placing them in a new variable, num_ethnic.
add_health_data['num_ethnic'] = add_health_data['H1GI4'] + add_health_data['H1GI6A'] + add_health_data['H1GI6B'] + add_health_data['H1GI6C'] + add_health_data['H1GI6D']

# Counting all instances of each value in the num_ethnic variable. 
count1 = add_health_data['num_ethnic'].value_counts(sort=True)
print(count1)

# This statement returns a number corrisponding to each ethnicity.
def ethnicity (row):
    if row ['num_ethnic'] > 1:
        return 1 
    if row ['H1GI4'] == 1: 
        return 2 
    if row ['H1GI6A'] == 1: 
        return 3
    if row ['H1GI6B'] == 1: 
        return 4
    if row ['H1GI6C'] == 1: 
        return 5
    if row ['H1GI6D'] == 1: 
        return 6

add_health_data['ethnicity'] = add_health_data.apply(lambda row: ethnicity (row), axis=1)    

# Outputting a grid that shows 25 random rows and what ethnicity they were identified as.
ethnicity_sub = add_health_data[['H1GI4','H1GI6A','H1GI6B','H1GI6C','H1GI6D','num_ethnic','ethnicity']]  
grid = ethnicity_sub.head(n=25)
print(grid)

# Counting the amount of children that were identified as Mixed Race.
add_health_data['ethnicity_count'] = ethnicity_sub['ethnicity'] == 1
mixed_subset = add_health_data['ethnicity_count'].sum()
print('Number of children who identified as Mixed Race: %s'  % (mixed_subset))

# Counting the amount of children that were identified as Latino.
add_health_data['ethnicity_count'] = ethnicity_sub['ethnicity'] == 2
latino_subset = add_health_data['ethnicity_count'].sum()
print('Number of children who identified as Latino: %s'  % (latino_subset))

# Counting the amount of children that were identified as White.
add_health_data['ethnicity_count'] = ethnicity_sub['ethnicity'] == 3
white_subset = add_health_data['ethnicity_count'].sum()
print('Number of children who identified as White: %s' % (white_subset))

# Counting the amount of children that were identified as Black / African American.
add_health_data['ethnicity_count'] = ethnicity_sub['ethnicity'] == 4
black_subset = add_health_data['ethnicity_count'].sum()
print('Number of children who identified as Black or African American: %s' % (black_subset))

# Counting the amount of children that were identified as American Indian / Native American.
add_health_data['ethnicity_count'] = ethnicity_sub['ethnicity'] == 5
indian_subset = add_health_data['ethnicity_count'].sum()
print('Number of children who identified as American Indian / Native American: %s' % (indian_subset))

# Counting the amount of children that were identified as Asian / Pacific Islander.
add_health_data['ethnicity_count'] = ethnicity_sub['ethnicity'] == 6
asian_subset = add_health_data['ethnicity_count'].sum()
print('Number of children who identified as Asian / Pacific Islander: %s' % (asian_subset))












## ## ## ## ## ---- Creating two subsets of kids. One where the kids feel safe in their neighbourhood and the other where they do not. ---- ## ## ## ## ##

# Converting H1NB5 to a number. 
add_health_data['H1NB5'] = pandas.to_numeric(add_health_data['H1NB5'])

# Extracting the records where the kids feel unsafe in their neighborhood. 
print('The number of kids that do not feel safe in their neighbourhood.')
unsafe_subset = add_health_data[(add_health_data['H1NB5'] == 0)]
print(len(unsafe_subset))

# Extracting the records where the kids feel safe in their neighborhood. 
print('The number of kids that do feel safe in their neighbourhood.')
safe_subset = add_health_data[(add_health_data['H1NB5'] == 1)]
print(len(safe_subset))



























