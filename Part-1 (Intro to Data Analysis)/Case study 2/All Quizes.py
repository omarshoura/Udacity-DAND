# Cleaning Column Labels
Use `all_alpha_08.csv` and `all_alpha_18.csv`

# load datasets
import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv') 
df_18 = pd.read_csv('all_alpha_18.csv')

# view 2008 dataset
df_08.head(1)

# view 2018 dataset
df_18.head(1)

### Drop Extraneous Columns

# drop columns from 2008 dataset
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)

# confirm changes
df_08.head(1)

# drop columns from 2018 dataset
df_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1, inplace=True)

# confirm changes
df_18.head(1)

### Rename Columns

# rename Sales Area to Cert Region
df_08.rename(columns={'Sales Area': 'Cert Region'}, inplace=True)

# confirm changes
df_08.head(1)

# replace spaces with underscores and lowercase labels for 2008 dataset
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df_08.head(1)

# replace spaces with underscores and lowercase labels for 2018 dataset
df_18.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df_18.head(1)

# confirm column labels for 2008 and 2018 datasets are identical
df_08.columns == df_18.columns

# make sure they're all identical like this
(df_08.columns == df_18.columns).all()

# save new datasets for next section
df_08.to_csv('data_08_v1.csv', index=False)
df_18.to_csv('data_18_v1.csv', index=False)

________________________________________________________________________________

# Drawing Conclusions
Use the space below to address questions on datasets `clean_08.csv` and `clean_18.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 3*.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
# load datasets

df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')
df_08.tail()

### Q1: Are more unique models using alternative sources of fuel? By how much?

df_08.model.nunique()

df_18.model.nunique()

df_08.fuel.value_counts()

df_18.fuel.value_counts()

alt_08=df_08.query("fuel in ['ethanol','CNG'] ").model.nunique()

alt_18=df_18.query("fuel in ['Ethanol','Electricity'] ").model.nunique()

plt.bar(["2008","2018"],[alt_08 , alt_18])
plt.title("Number of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Number of Unique Models");



### Q2: How much have vehicle classes improved in fuel economy?  

mpg_08=df_08.groupby('veh_class').mean()['cmb_mpg']
mpg_08

mpg_18=df_18.groupby('veh_class').mean()['cmb_mpg']
mpg_18

inc= mpg_18-mpg_08
inc.dropna(inplace=True)
inc

plt.subplots(figsize=(8, 5))
plt.bar(inc.index,inc);
plt.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Increase in Average Combined MPG');

### Q3: What are the characteristics of SmartWay vehicles? Have they changed over time?

smrt_08=df_08.query('smartway in ["yes" , "Elite"]').describe().loc['mean','cmb_mpg':]
# smrt.groupby('smartway')
smrt_08

smrt_18=df_18.query('smartway in ["yes" , "Elite"]').describe().loc['mean','cmb_mpg':]
# smrt.groupby('smartway')
smrt_18

imp=smrt_18-smrt_08
imp

plt.subplots(figsize=(5, 4))
plt.bar(imp.index,imp);
plt.title('imp in smrt way');
plt.xlabel('char')
plt.ylabel('val');

### Q4: What features are associated with better fuel economy?

top_08=df_08.query('cmb_mpg > cmb_mpg.mean()').describe().loc['mean']

top_18=df_18.query('cmb_mpg > cmb_mpg.mean()').describe().loc['mean']

plt.subplots(figsize=(12,4));
plt.bar(top_08.index,top_08)


plt.subplots(figsize=(12,4));
plt.bar(top_18.index,top_18);

________________________________________________________________________________

# Exploring with Visuals
Use `clean_08.csv` and `clean_18.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 3*.

import pandas as pd
import matplotlib.pyplot as plt
# load datasets

df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')
df_08.head(5)

df_08.greenhouse_gas_score.hist();

df_18.greenhouse_gas_score.hist();

df_08.cmb_mpg.hist();

df_18.cmb_mpg.hist();

df_08['displ'].corr(df_08['cmb_mpg']);
df_08.plot.scatter(x='cmb_mpg',y='displ')

df_08['displ'].corr(df_08['cmb_mpg']);
df_18.plot.scatter(x='cmb_mpg',y='displ')
________________________________________________________________________________

# Filter, Drop Nulls, Dedupe
Use `data_08_v1.csv` and `data_18_v1.csv`

# load datasets
import pandas as pd

df_08 = pd.read_csv('data_08_v1.csv')
df_18 = pd.read_csv('data_18_v1.csv')

# view dimensions of dataset
df_08.shape

# view dimensions of dataset
df_18.shape

## Filter by Certification Region

# filter datasets for rows following California standards
df_08 = df_08.query('cert_region == "CA"')
df_18 = df_18.query('cert_region == "CA"')

# confirm only certification region is California
df_08['cert_region'].unique()

# confirm only certification region is California
df_18['cert_region'].unique()

# drop certification region columns form both datasets
df_08.drop('cert_region', axis=1, inplace=True)
df_18.drop('cert_region', axis=1, inplace=True)

df_08.shape

df_18.shape

## Drop Rows with Missing Values

# view missing value count for each feature in 2008
df_08.isnull().sum()

# view missing value count for each feature in 2018
df_18.isnull().sum()

# drop rows with any null values in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)

# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()

# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()

## Dedupe Data

# print number of duplicates in 2008 and 2018 datasets
print(df_08.duplicated().sum())
print(df_18.duplicated().sum())

# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)

# print number of duplicates again to confirm dedupe - should both be 0
print(df_08.duplicated().sum())
print(df_18.duplicated().sum())

# save progress for the next section
df_08.to_csv('data_08_v2.csv', index=False)
df_18.to_csv('data_18_v2.csv', index=False)

________________________________________________________________________________

# Fixing `air_pollution_score` Data Type
- 2008: convert string to float
- 2018: convert int to float

Load datasets `data_08_v3.csv` and `data_18_v3.csv`.

# load datasets
import pandas as pd

df_08 = pd.read_csv('data_08_v3.csv')
df_18 = pd.read_csv('data_18_v3.csv')

# try using Pandas to_numeric or astype function to convert the
# 2008 air_pollution_score column to float -- this won't work
df_08.air_pollution_score = df_08.air_pollution_score.astype(float)

# Figuring out the issue
Looks like this isn't going to be as simple as converting the datatype. According to the error above, the air pollution score value in one of the rows is "6/4" - let's check it out.

df_08[df_08.air_pollution_score == '6/4']

# It's not just the air pollution score!
The mpg columns and greenhouse gas scores also seem to have the same problem - maybe that's why these were all saved as strings! According to [this link](http://www.fueleconomy.gov/feg/findacarhelp.shtml#airPollutionScore), which I found from the PDF documentation:

    "If a vehicle can operate on more than one type of fuel, an estimate is provided for each fuel type."
    
Ohh.. so all vehicles with more than one fuel type, or hybrids, like the one above (it uses ethanol AND gas) will have a string that holds two values - one for each. This is a little tricky, so I'm going to show you how to do it with the 2008 dataset, and then you'll try it with the 2018 dataset.

# First, let's get all the hybrids in 2008
hb_08 = df_08[df_08['fuel'].str.contains('/')]
hb_08

Looks like this dataset only has one! The 2018 has MANY more - but don't worry - the steps I'm taking here will work for that as well!

# hybrids in 2018
hb_18 = df_18[df_18['fuel'].str.contains('/')]
hb_18

We're going to take each hybrid row and split them into two new rows - one with values for the first fuel type (values before the "/"), and the other with values for the second fuel type (values after the "/"). Let's separate them with two dataframes!

# create two copies of the 2008 hybrids dataframe
df1 = hb_08.copy()  # data on first fuel type of each hybrid vehicle
df2 = hb_08.copy()  # data on second fuel type of each hybrid vehicle

# Each one should look like this
df1

For this next part, we're going use Pandas' apply function. See the docs [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html).

# columns to split by "/"
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg', 'greenhouse_gas_score']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

# this dataframe holds info for the FIRST fuel type of the hybrid
# aka the values before the "/"s
df1

# this dataframe holds info for the SECOND fuel type of the hybrid
# aka the values before the "/"s
df2

# combine dataframes to add to the original dataframe
new_rows = df1.append(df2)

# now we have separate rows for each fuel type of each vehicle!
new_rows

# drop the original hybrid rows
df_08.drop(hb_08.index, inplace=True)

# add in our newly separated rows
df_08 = df_08.append(new_rows, ignore_index=True)

# check that all the original hybrid rows with "/"s are gone
df_08[df_08['fuel'].str.contains('/')]

df_08.shape

# Repeat this process for the 2018 dataset

# create two copies of the 2018 hybrids dataframe, hb_18
df1 = hb_18.copy()
df2 = hb_18.copy()

### Split values for `fuel`, `city_mpg`, `hwy_mpg`, `cmb_mpg`
You don't need to split for `air_pollution_score` or `greenhouse_gas_score` here because these columns are already ints in the 2018 dataset.

# list of columns to split
split_columns = ['fuel', 'city_mpg', 'hwy_mpg', 'cmb_mpg']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

# append the two dataframes
new_rows = df1.append(df2)

# drop each hybrid row from the original 2018 dataframe
# do this by using Pandas drop function with hb_18's index
df_18.drop(hb_18.index, inplace=True)

# append new_rows to df_18
df_18 = df_18.append(new_rows, ignore_index=True)

# check that they're gone
df_18[df_18['fuel'].str.contains('/')]

df_18.shape

### Now we can comfortably continue the changes needed for `air_pollution_score`! Here they are again:
- 2008: convert string to float
- 2018: convert int to float

# convert string to float for 2008 air pollution column
df_08.air_pollution_score = df_08.air_pollution_score.astype(float)

# convert int to float for 2018 air pollution column
df_18.air_pollution_score = df_18.air_pollution_score.astype(float)

df_08.to_csv('data_08_v4.csv', index=False)
df_18.to_csv('data_18_v4.csv', index=False)

________________________________________________________________________________

# Fixing `cyl` Data Type
- 2008: extract int from string
- 2018: convert float to int

Load datasets `data_08_v2.csv` and `data_18_v2.csv`.

# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v2.csv')
df_18 = pd.read_csv('data_18_v2.csv') 

# check value counts for the 2008 cyl column
df_08['cyl'].value_counts()

Read [this](https://stackoverflow.com/questions/35376387/extract-int-from-string-in-pandas) to help you extract ints from strings in Pandas for the next step.

# Extract int from strings in the 2008 cyl column
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)

# Check value counts for 2008 cyl column again to confirm the change
df_08['cyl'].value_counts()

# convert 2018 cyl column to int
df_18['cyl'] = df_18['cyl'].astype(int)

df_08.to_csv('data_08_v3.csv', index=False)
df_18.to_csv('data_18_v3.csv', index=False)

________________________________________________________________________________

## Fix `city_mpg`, `hwy_mpg`, `cmb_mpg` datatypes
    2008 and 2018: convert string to float

Load datasets `data_08_v4.csv` and `data_18_v4.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 2*.

import pandas as pd
# load datasets

df_08 = pd.read_csv('data_08_v4.csv')
df_18 = pd.read_csv('data_18_v4.csv')
df_08.head(5)

# convert mpg columns to floats
mpg_columns = ['city_mpg','hwy_mpg','cmb_mpg']
for c in mpg_columns:
    df_18[c] = df_18[c].astype(float)
    df_08[c] = df_08[c].astype(float)

## Fix `greenhouse_gas_score` datatype
    2008: convert from float to int

# convert from float to int
df_08['greenhouse_gas_score'] = df_08.greenhouse_gas_score.astype('int64')

## All the dataypes are now fixed! Take one last check to confirm all the changes.

df_08.dtypes

df_18.dtypes

df_08.dtypes == df_18.dtypes

# Save your final CLEAN datasets as new files!
df_08.to_csv('clean_08.csv', index=False)
df_18.to_csv('clean_18.csv', index=False)

________________________________________________________________________________

# Merging Datasets
Use pandas Merges to create a combined dataset from `clean_08.csv` and `clean_18.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 3*.

import pandas as pd
# load datasets

df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')

### Create combined dataset

# rename 2008 columns
df_08.rename(columns=lambda x:x[:10]+"_2008")

# view to check names
df_08.head()

# merge datasets
df_combined = df_08.merge(df_18,left_on='model_2008',right_on='model',how='inner')
# merge datasets
df_combined = df_08.merge(df_18, left_on='model_2008', right_on='model', how='inner')

# view to check merge
df_combined.head()

df_combined.shape

Save the combined dataset

df_combined.to_csv('combined_dataset.csv', index=False)

________________________________________________________________________________

# Results with Merged Dataset
#### Q5: For all of the models that were produced in 2008 that are still being produced now, how much has the mpg improved and which vehicle improved the most?
Remember to use your new dataset, `combined_dataset.csv`. You should've created this data file in the previous section: *Merging Datasets*.

import pandas as pd
# load dataset

df = pd.read_csv('combined_dataset.csv')


### 1. Create a new dataframe, `model_mpg`, that contain the mean combined mpg values in 2008 and 2018 for each unique model

To do this, group by `model` and find the mean `cmb_mpg_2008` and mean `cmb_mpg` for each.

model_mpg = df.groupby('model').mean()
model_mpg['cmb_mpg_2008']

### 2. Create a new column, `mpg_change`, with the change in mpg
Subtract the mean mpg in 2008 from that in 2018 to get the change in mpg

model_mpg['mpg_change'] = model_mpg.cmb_mpg-model_mpg.cmb_mpg_2008

model_mpg.head()

### 3. Find the vehicle that improved the most
Find the max mpg change, and then use query or indexing to see what model it is!

model_mpg.mpg_change.max()

model_mpg.query('mpg_change==16.53333333333334')