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



## ## ## ## ## ---- Neighbourhood Section Frequency Distributions Dataset ---- ## ## ## ## ##
## Question 5
print('Counts for H1NB5 - Do you usually feel safe in your neighborhood? Yes = 1')
nb_count_5 = add_health_data['H1NB5'].value_counts(sort=True)
print(nb_count_5) 

print('Percentages for H1NB5 - Do you usually feel safe in your neighborhood? Yes = 1')
nb_percentage_5 = add_health_data['H1NB5'].value_counts(sort=True, normalize=True)
print(nb_percentage_5)



## ## ## ## ## ---- Fighting & Violence Section Frequency Distributions Dataset ---- ## ## ## ## ##
## During the past 12 months how often did each of the following things happen?
## Question 1 
print('Counts for H1FV1 - You saw someone shoot or stab another person.')
fv_count_1 = add_health_data['H1FV1'].value_counts(sort=True)
print(fv_count_1) 

print('Percentages for H1FV1 - You saw someone shoot or stab another person.')
fv_percentage_1 = add_health_data['H1FV1'].value_counts(sort=True, normalize=True)
print(fv_percentage_1)

## Question 2
print('Counts for H1FV2 - Someone pulled a knife or gun on you.')
fv_count_2 = add_health_data['H1FV2'].value_counts(sort=True)
print(fv_count_2) 

print('Percentages for H1FV2 - Someone pulled a knife or gun on you.')
fv_percentage_2 = add_health_data['H1FV2'].value_counts(sort=True, normalize=True)
print(fv_percentage_2)

## Question 3
print('Counts for H1FV3 - Someone shot you.')
fv_count_3 = add_health_data['H1FV3'].value_counts(sort=True)
print(fv_count_3) 

print('Percentages for H1FV3 - Someone shot you.')
fv_percentage_3 = add_health_data['H1FV3'].value_counts(sort=True, normalize=True)
print(fv_percentage_3)

## Question 4
print('Counts for H1FV4 - Someone cut or stabbed you.')
fv_count_4 = add_health_data['H1FV4'].value_counts(sort=True)
print(fv_count_4) 

print('Percentages for H1FV4 - Someone cut or stabbed you.')
fv_percentage_4 = add_health_data['H1FV4'].value_counts(sort=True, normalize=True)
print(fv_percentage_4)

## Question 5
print('Counts for H1FV5 - You got into a physical fight.')
fv_count_5 = add_health_data['H1FV5'].value_counts(sort=True)
print(fv_count_5) 

print('Percentages for H1FV5 - You got into a physical fight.')
fv_percentage_5 = add_health_data['H1FV5'].value_counts(sort=True, normalize=True)
print(fv_percentage_5)

## Question 6
print('Counts for H1FV6 - You were jumped.')
fv_count_6 = add_health_data['H1FV6'].value_counts(sort=True)
print(fv_count_6) 

print('Percentages for H1FV6 - You were jumped.')
fv_percentage_6 = add_health_data['H1FV6'].value_counts(sort=True, normalize=True)
print(fv_percentage_6)

## Question 7
print('Counts for H1FV7 - You pulled a knife or gun on someone.')
fv_count_7 = add_health_data['H1FV7'].value_counts(sort=True)
print(fv_count_7) 

print('Percentages for H1FV7 - You pulled a knife or gun on someone.')
fv_percentage_7 = add_health_data['H1FV7'].value_counts(sort=True, normalize=True)
print(fv_percentage_7)

## Question 8
print('Counts for H1FV8 - You shot or stabbed someone.')
fv_count_8 = add_health_data['H1FV8'].value_counts(sort=True)
print(fv_count_8) 

print('Percentages for H1FV8 - You shot or stabbed someone.')
fv_percentage_8 = add_health_data['H1FV8'].value_counts(sort=True, normalize=True)
print(fv_percentage_8)

## Question 9
print('Counts for H1FV9 - During the past 30 days, on how many days did you carry a weapon—such as a gun, knife, or club—to school?')
fv_count_9 = add_health_data['H1FV9'].value_counts(sort=True)
print(fv_count_9) 

print('Percentages for H1FV9 - During the past 30 days, on how many days did you carry a weapon—such as a gun, knife, or club—to school?')
fv_percentage_9 = add_health_data['H1FV9'].value_counts(sort=True, normalize=True)
print(fv_percentage_9)

## Question 10
print('Counts for H1FV10 - During the past 30 days, what one kind of weapon did you carry most often to school?')
fv_count_10 = add_health_data['H1FV10'].value_counts(sort=True)
print(fv_count_10) 

print('Percentages for H1FV10 - During the past 30 days, what one kind of weapon did you carry most often to school?')
fv_percentage_10 = add_health_data['H1FV10'].value_counts(sort=True, normalize=True)
print(fv_percentage_10)



## ## ## ## ## ---- General Introductory Section Frequency Distributions Dataset ---- ## ## ## ## ##
## Question 9
print('Counts for H1GI9 - Interviewer: Please code the race of the respondent from your own observation alone.')
gi_count_1 = add_health_data['H1GI9'].value_counts(sort=True)
print(gi_count_1) 

print('Percentages for H1GI9 - Interviewer: Please code the race of the respondent from your own observation alone.')
gi_percentage_1 = add_health_data['H1GI9'].value_counts(sort=True, normalize=True)
print(gi_percentage_1)



## ## ## ## ## ---- Reducing Dataset To Kids Who Do Not Feel Safe In There Neighborhood ---- ## ## ## ## ##

# Converting H1NB5 to a number 
add_health_data['H1NB5'] = pandas.to_numeric(add_health_data['H1NB5'], errors='ignore')

# Extracting the records where the kids feel unsafe in their neighborhood.
print('The number of rows in the subset of kids who do not feel safe in their neighborhood.')
unsafe_subset = add_health_data[(add_health_data['H1NB5'] == 0)]
print(len(unsafe_subset))

# Generating a distribution frequency on the subset based on the kids grade in school. 
print('Counts for H1GI20 - Grade kids are in.')
grade_count = unsafe_subset['H1GI20'].value_counts(sort=True)
print (grade_count)

print('Percentages for H1GI20 - Grade kids are in.')
grade_percentage = unsafe_subset['H1GI20'].value_counts(sort=True, normalize=True)
print (grade_percentage)

# Making a copy of the unsafe_subset 
unsafe_subset_copy = unsafe_subset.copy()



## ## ## ## ## ---- Checking and removing any missing or unnessicary data form the Fighting & Violence Data ---- ## ## ## ## ##

# Checking to make sure the F&V data are numberic
unsafe_subset_copy['H1FV1']=pandas.to_numeric(unsafe_subset_copy['H1FV1'])
unsafe_subset_copy['H1FV2']=pandas.to_numeric(unsafe_subset_copy['H1FV2'])
unsafe_subset_copy['H1FV3']=pandas.to_numeric(unsafe_subset_copy['H1FV3'])
unsafe_subset_copy['H1FV4']=pandas.to_numeric(unsafe_subset_copy['H1FV4'])
unsafe_subset_copy['H1FV5']=pandas.to_numeric(unsafe_subset_copy['H1FV5'])
unsafe_subset_copy['H1FV6']=pandas.to_numeric(unsafe_subset_copy['H1FV6'])
unsafe_subset_copy['H1FV7']=pandas.to_numeric(unsafe_subset_copy['H1FV7'])
unsafe_subset_copy['H1FV8']=pandas.to_numeric(unsafe_subset_copy['H1FV8'])
unsafe_subset_copy['H1FV9']=pandas.to_numeric(unsafe_subset_copy['H1FV9'])
unsafe_subset_copy['H1FV10']=pandas.to_numeric(unsafe_subset_copy['H1FV10'])

### --- --- H1FV1 --- --- ###

# Counting all values for the H1FV1
print('Counts for H1FV1 - You saw someone shoot or stab another person.')
subset_fv1_count=unsafe_subset_copy['H1FV1'].value_counts(sort=True)
print(subset_fv1_count)

# Removing option 6 from H1FV1 - refused
unsafe_subset_copy['H1FV1'] = unsafe_subset_copy['H1FV1'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV1']==6).sum())
  
# Removing option 8 H1FV1 - don't know 
unsafe_subset_copy['H1FV1'] = unsafe_subset_copy['H1FV1'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV1']==8).sum())

### --- --- H1FV2 --- --- ###

# Counting all values for the H1FV2
print('Counts for H1FV2 - Someone pulled a knife or gun on you.')
subset_fv2_count=unsafe_subset_copy['H1FV2'].value_counts(sort=True)
print(subset_fv2_count)

# Removing option 6 from H1FV2 - refused
unsafe_subset_copy['H1FV2'] = unsafe_subset_copy['H1FV2'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV2']==6).sum())
  
# Removing option 8 H1FV2 - don't know 
unsafe_subset_copy['H1FV2'] = unsafe_subset_copy['H1FV2'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV2']==8).sum())

### --- --- H1FV3 --- --- ###

# Counting all values for the H1FV3
print('Counts for H1FV3 - Someone shot you.')
subset_fv3_count=unsafe_subset_copy['H1FV3'].value_counts(sort=True)
print(subset_fv3_count)

# Removing option 6 from H1FV3 - refused
unsafe_subset_copy['H1FV3'] = unsafe_subset_copy['H1FV3'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV3']==6).sum())
  
# Removing option 8 H1FV3 - don't know 
unsafe_subset_copy['H1FV3'] = unsafe_subset_copy['H1FV3'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV3']==8).sum())

### --- --- H1FV4 --- --- ###

# Counting all values for the H1FV4
print('Counts for H1FV4 - Someone cut or stabbed you.')
subset_fv4_count=unsafe_subset_copy['H1FV4'].value_counts(sort=True)
print(subset_fv4_count)

# Removing option 6 from H1FV4 - refused
unsafe_subset_copy['H1FV4'] = unsafe_subset_copy['H1FV4'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV4']==6).sum())
  
# Removing option 8 H1FV4 - don't know 
unsafe_subset_copy['H1FV4'] = unsafe_subset_copy['H1FV4'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV4']==8).sum())

### --- --- H1FV5 --- --- ###

# Counting all values for the H1FV5
print('Counts for H1FV5 - You got into a physical fight.')
subset_fv5_count=unsafe_subset_copy['H1FV5'].value_counts(sort=True)
print(subset_fv5_count)

# Removing option 6 from H1FV5 - refused
unsafe_subset_copy['H1FV5'] = unsafe_subset_copy['H1FV5'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV5']==6).sum())
  
# Removing option 8 H1FV5 - don't know 
unsafe_subset_copy['H1FV5'] = unsafe_subset_copy['H1FV5'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV5']==8).sum())

### --- --- H1FV6 --- --- ###

# Counting all values for the H1FV6
print('Counts for H1FV6 - You were jumped.')
subset_fv6_count=unsafe_subset_copy['H1FV6'].value_counts(sort=True)
print(subset_fv6_count)

# Removing option 6 from H1FV6 - refused
unsafe_subset_copy['H1FV6'] = unsafe_subset_copy['H1FV6'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV6']==6).sum())
  
# Removing option 8 H1FV6 - don't know 
unsafe_subset_copy['H1FV6'] = unsafe_subset_copy['H1FV6'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV6']==8).sum())

### --- --- H1FV7 --- --- ###

# Counting all values for the H1FV7
print('Counts for H1FV7 - You pulled a knife or gun on someone.')
subset_fv7_count=unsafe_subset_copy['H1FV7'].value_counts(sort=True)
print(subset_fv7_count)

# Removing option 6 from H1FV7 - refused
unsafe_subset_copy['H1FV7'] = unsafe_subset_copy['H1FV7'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV7']==6).sum())
  
# Removing option 8 H1FV7 - don't know 
unsafe_subset_copy['H1FV7'] = unsafe_subset_copy['H1FV7'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV7']==8).sum())

### --- --- H1FV8 --- --- ###

# Counting all values for the H1FV8
print('Counts for H1FV8 - You shot or stabbed someone.')
subset_fv8_count=unsafe_subset_copy['H1FV8'].value_counts(sort=True)
print(subset_fv8_count)

# Removing option 6 from H1FV8 - refused
unsafe_subset_copy['H1FV8'] = unsafe_subset_copy['H1FV8'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV8']==6).sum())
  
# Removing option 8 H1FV8 - don't know 
unsafe_subset_copy['H1FV8'] = unsafe_subset_copy['H1FV8'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV8']==8).sum())

### --- --- H1FV9 --- --- ###

# Counting all values for the H1FV9
print('Counts for H1FV9 - During the past 30 days, on how many days did you carry a weapon—such as a gun, knife, or club—to school?')
subset_fv9_count=unsafe_subset_copy['H1FV9'].value_counts(sort=True)
print(subset_fv9_count)

# Removing option 6 from H1FV9 - refused
unsafe_subset_copy['H1FV9'] = unsafe_subset_copy['H1FV9'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV9']==6).sum())
  
# Removing option 8 H1FV9 - don't know 
unsafe_subset_copy['H1FV9'] = unsafe_subset_copy['H1FV9'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV9']==8).sum())

### --- --- H1FV10 --- --- ###

# Counting all values for the H1FV10
print('Counts for H1FV10 - During the past 30 days, what one kind of weapon did you carry most often to school?')
subset_fv10_count=unsafe_subset_copy['H1FV10'].value_counts(sort=True, dropna=False)
print(subset_fv10_count)

# Removing option 6 from H1FV10 - refused
unsafe_subset_copy['H1FV10'] = unsafe_subset_copy['H1FV10'].replace(6,numpy.nan)
print((unsafe_subset_copy['H1FV10']==6).sum())

# Removing option 7 from H1FV10 - refused
unsafe_subset_copy['H1FV10'] = unsafe_subset_copy['H1FV10'].replace(7,numpy.nan)
print((unsafe_subset_copy['H1FV10']==7).sum())
  
# Removing option 8 H1FV10 - don't know 
unsafe_subset_copy['H1FV10'] = unsafe_subset_copy['H1FV10'].replace(8,numpy.nan)
print((unsafe_subset_copy['H1FV10']==8).sum())

subset3 = unsafe_subset_copy[['H1FV10', 'H1FV9', 'H1FV8']]
subset3.head(25)



## ## ## ## ## ---- Determining the Childrens Ethnicity ---- ## ## ## ## ##

# Making sure all data is numeric. 
unsafe_subset_copy['H1GI4']=pandas.to_numeric(unsafe_subset_copy['H1GI4'])
unsafe_subset_copy['H1GI6A']=pandas.to_numeric(unsafe_subset_copy['H1GI6A'])
unsafe_subset_copy['H1GI6B']=pandas.to_numeric(unsafe_subset_copy['H1GI6B'])
unsafe_subset_copy['H1GI6C']=pandas.to_numeric(unsafe_subset_copy['H1GI6C'])
unsafe_subset_copy['H1GI6D']=pandas.to_numeric(unsafe_subset_copy['H1GI6D'])

# Removing unused values.
unsafe_subset_copy['H1GI4'] = unsafe_subset_copy['H1GI4'].replace([6,8],numpy.nan)
unsafe_subset_copy['H1GI6A'] = unsafe_subset_copy['H1GI6A'].replace([6,8],numpy.nan)
unsafe_subset_copy['H1GI6B'] = unsafe_subset_copy['H1GI6B'].replace([6,8],numpy.nan)
unsafe_subset_copy['H1GI6C'] = unsafe_subset_copy['H1GI6C'].replace([6,8],numpy.nan)
unsafe_subset_copy['H1GI6D'] = unsafe_subset_copy['H1GI6D'].replace([6,8],numpy.nan)

# Summing each of the variables and placing them in a new variales called num_ethnic.
unsafe_subset_copy['num_ethnic'] = unsafe_subset_copy['H1GI4'] + unsafe_subset_copy['H1GI6A'] + unsafe_subset_copy['H1GI6B'] + unsafe_subset_copy['H1GI6C'] + unsafe_subset_copy['H1GI6D']

# Counting all instances of each value for num_ethnic variable. 
count1=unsafe_subset_copy['num_ethnic'].value_counts(sort=True)
print(count1)












































