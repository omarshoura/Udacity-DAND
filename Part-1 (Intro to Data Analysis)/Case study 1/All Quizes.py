# Drawing Conclusions Using Query

# Load 'winequality_edited.csv,' a file you created in a previous section 
import pandas as pd

df = pd.read_csv('winequality_edited.csv')
df.head()

### Do wines with higher alcoholic content receive better ratings?

# get the median amount of alcohol content
df.alcohol.median()

# select samples with alcohol content less than the median
low_alcohol = df.query('alcohol < 10.3')

# select samples with alcohol content greater than or equal to the median
high_alcohol = df.query('alcohol >= 10.3')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() # should be True

# get mean quality rating for the low alcohol and high alcohol groups
low_alcohol.quality.mean(), high_alcohol.quality.mean()

### Do sweeter wines receive better ratings?

# get the median amount of residual sugar
df.residual_sugar.median()

# select samples with residual sugar less than the median
low_sugar = df.query('residual_sugar < 3')

# select samples with residual sugar greater than or equal to the median
high_sugar = df.query('residual_sugar >= 3')

# ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count() # should be True

# get mean quality rating for the low sugar and high sugar groups
low_sugar.quality.mean(), high_sugar.quality.mean()

_____________________________________________________________________________________________________

# Plotting Wine Type and Quality with Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')

wine_df = pd.read_csv('winequality_edited.csv')

### Create arrays for red bar heights white bar heights
Remember, there's a bar for each combination of color and quality rating. Each bar's height is based on the proportion of samples of that color with that quality rating.
1. Red bar proportions = counts for each quality rating / total # of red samples
2. White bar proportions = counts for each quality rating / total # of white samples

# get counts for each rating and color
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
color_counts

# get total counts for each color
color_totals = wine_df.groupby('color').count()['pH']
color_totals

# get proportions by dividing red rating counts by total # of red samples
red_proportions = color_counts['red'] / color_totals['red']
red_proportions

# get proportions by dividing white rating counts by total # of white samples
white_proportions = color_counts['white'] / color_totals['white']
white_proportions

### Plot proportions on a bar chart
Set the x coordinate location for each rating group and and width of each bar.

ind = np.arange(len(red_proportions))  # the x locations for the groups
width = 0.35       # the width of the bars

Now let’s create the plot.

# plot bars
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# title and labels
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # xtick locations
labels = ['3', '4', '5', '6', '7', '8', '9']  # xtick labels
plt.xticks(locations, labels)

# legend
plt.legend()

Oh, that didn't work because we're missing a red wine value for a the 9 rating. Even though this number is a 0, we need it for our plot. Run the last two cells after running the cell below.

red_proportions['9'] = 0
red_proportions

_____________________________________________________________________________________________________


# Creating a Bar Chart Using Matplotlib

import matplotlib.pyplot as plt
% matplotlib inline

There are two required arguments in pyplot's `bar` function: the x-coordinates of the bars, and the heights of the bars.

plt.bar([1, 2, 3], [224, 620, 425]);

You can specify the x tick labels using pyplot's `xticks` function, or by specifying another parameter in the `bar` function. The two cells below accomplish the same thing.

# plot bars
plt.bar([1, 2, 3], [224, 620, 425])

# specify x coordinates of tick labels and their labels
plt.xticks([1, 2, 3], ['a', 'b', 'c']);

# plot bars with x tick labels
plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c']);

Set the title and label axes like this.

plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c'])
plt.title('Some Title')
plt.xlabel('Some X Label')
plt.ylabel('Some Y Label');

_____________________________________________________________________________________________________

# Plotting with Matplotlib
Use Matplotlib to create bar charts that visualize the conclusions you made with groupby and query.

# Import necessary packages and load `winequality_edited.csv`
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('winequality_edited.csv')

### #1: Do wines with higher alcoholic content receive better ratings?
Create a bar chart with one bar for low alcohol and one bar for high alcohol wine samples. This first one is filled out for you.

# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()

# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');

### #2: Do sweeter wines receive higher ratings?
Create a bar chart with one bar for low residual sugar and one bar for high residual sugar wine samples.

# Use query to select each group and get its mean quality
median=df.residual_sugar.median()
median
low_sugar=df.query('residual_sugar<{}'.format(median))
high_sugar=df.query('residual_sugar>={}'.format(median))
low=low_sugar['quality'].mean()
high=high_sugar['quality'].mean()
high_sugar.head()

# Create a bar chart with proper labels
heights=[low,high]
locations=[1,2]
colors=['gray','red']
labels=['low','high']
plt.bar(locations,heights,tick_label=labels,color=colors,width=0.4);
plt.ylim(0,6.2);


### #3: What level of acidity receives the highest average rating?
Create a bar chart with a bar for each of the four acidity levels.

# Use groupby to get the mean quality for each acidity level
x=list(df.groupby('acidity_levels')['quality'].mean())
x

# Create a bar chart with proper labels
locations=[1,2,3,4]
plt.bar(locations,x)
plt.ylim(0,6.5)


### Bonus: Create a line plot for the data in #3
You can use pyplot's [plot](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) function for this.



Compare this with the bar chart. How might showing this visual instead of the bar chart affect someone's conclusion about this data?