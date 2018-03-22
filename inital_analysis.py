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
## Question 1 
print('Counts for H1NB1 - You know most of the people in your neighborhood. True = 1')
nb_count_1 = add_health_data['H1NB1'].value_counts(sort=True)
print(nb_count_1) 

print('Percentages for H1NB1 - You know most of the people in your neighborhood. True = 1')
nb_percentage_1 = add_health_data['H1NB1'].value_counts(sort=True, normalize=True)
print(nb_percentage_1)

## Question 2
print('Counts for H1NB2 - In the past month, you have stopped on the street to talk with someone who lives in your neighborhood. True = 1')
nb_count_2 = add_health_data['H1NB2'].value_counts(sort=True)
print(nb_count_2) 

print('Percentages for H1NB2 - In the past month, you have stopped on the street to talk with someone who lives in your neighborhood. True = 1')
nb_percentage_2 = add_health_data['H1NB2'].value_counts(sort=True, normalize=True)
print(nb_percentage_2)

## Question 3
print('Counts for H1NB3 - People in this neighborhood look out for each other. True = 1')
nb_count_3 = add_health_data['H1NB3'].value_counts(sort=True)
print(nb_count_3) 

print('Percentages for H1NB3 - People in this neighborhood look out for each other. True = 1')
nb_percentage_3 = add_health_data['H1NB3'].value_counts(sort=True, normalize=True)
print(nb_percentage_3)

## Question 4
print('Counts for H1NB4 - Do you use a physical fitness or recreation center in your neighborhood? Yes = 1')
nb_count_4 = add_health_data['H1NB4'].value_counts(sort=True)
print(nb_count_4) 

print('Percentages for H1NB4 - Do you use a physical fitness or recreation center in your neighborhood? Yes = 1')
nb_percentage_4 = add_health_data['H1NB4'].value_counts(sort=True, normalize=True)
print(nb_percentage_4)

## Question 5
print('Counts for H1NB5 - Do you usually feel safe in your neighborhood? Yes = 1')
nb_count_5 = add_health_data['H1NB5'].value_counts(sort=True)
print(nb_count_5) 

print('Percentages for H1NB5 - Do you usually feel safe in your neighborhood? Yes = 1')
nb_percentage_5 = add_health_data['H1NB5'].value_counts(sort=True, normalize=True)
print(nb_percentage_5)

## Question 6 
print('Counts for H1NB6 - On the whole, how happy are you with living in your neighborhood?')
nb_count_6 = add_health_data['H1NB6'].value_counts(sort=True)
print(nb_count_6) 

print('Percentages for H1NB6 - On the whole, how happy are you with living in your neighborhood?')
nb_percentage_6 = add_health_data['H1NB6'].value_counts(sort=True, normalize=True)
print(nb_percentage_6)

## Question 7
print('Counts for H1NB7 - If, for any reason, you had to move from here to some other neighborhood, how happy or unbappy would you be?')
nb_count_7 = add_health_data['H1NB7'].value_counts(sort=True)
print(nb_count_7) 

print('Percentages for H1NB7 - If, for any reason, you had to move from here to some other neighborhood, how happy or unbappy would you be?')
nb_percentage_7 = add_health_data['H1NB7'].value_counts(sort=True, normalize=True)
print(nb_percentage_7)



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


















































