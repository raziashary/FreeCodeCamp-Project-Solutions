import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv('C:\Belajar Kode\FreeCodeCamp\Data Analytics\medical_examination.csv')

# Add 'overweight' column
def calculate_bmi(height, weight):
    # Convert height to meters
    height_meters = height / 100
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    return bmi

df['bmi'] = df.apply(lambda row: calculate_bmi(row['height'], row['weight']), axis=1)
df['bmi'] = df['bmi'].round(1)

bmi_threshold = 25
df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25 else 0 )

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    selected_columns = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, id_vars=['id', 'cardio'], value_vars=selected_columns, var_name='variable', value_name='value')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    
    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x='variable', hue='value', col='cardio', y='count', 
                data=df_cat, kind='bar', height=5, aspect=1.2)

    # Get the figure for the output
    fig = plt.gcf() 

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df
    df_heat = df_heat[df_heat['ap_lo'] <= df_heat['ap_hi']]

    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]

    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='icefire', 
                vmax=0.24, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
