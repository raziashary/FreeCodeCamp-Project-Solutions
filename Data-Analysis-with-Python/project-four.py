import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as py
from pandas.plotting import register_matplotlib_converters

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('C:\\Belajar Kode\\FreeCodeCamp\\Data Analytics\\fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index(df['date'])
df = df.drop(['date'], axis=1)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,6))
    ax.plot(df.index, df[df.columns[0]], color='red', label=df.columns[0])
    
    # Set the title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    #plt.tight_layout()
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Month'] = df_bar.index.month
    df_bar['Year'] = df_bar.index.year
    df_bar = df_bar.groupby(['Year', 'Month']).mean().round(0).reset_index()

    #Change month into name rather than numbers
    import calendar
    df_bar['Month'] = df_bar['Month'].apply(lambda x: calendar.month_name[int(x)])
    df_bar['Month'] = pd.Categorical(df_bar['Month'], categories=['January', 'February', 'March', 'April', 'May', 
                                                                'June', 'July', 'August', 'September', 'October',
                                                                'November', 'December'], ordered=True)
    df_bar

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 6))

    # Plot the bar chart and set color
    pal = sns.color_palette("magma", len(df_bar['Month'].unique()))
    sns.barplot(x='Year', y='value', hue='Month', data=df_bar, palette = pal, ci=None, ax=ax)

    # Set labels and title
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views per Month by Year')

    # Set legend title and position
    ax.legend(title='Months', loc='upper left')

    # Show plot
    #plt.tight_layout()
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month'] = pd.Categorical(df_box['month'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 
                                                              'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 
                                                              'Nov', 'Dec'], ordered=True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Plot the first box plot on the first subplot
    palette_axes0 = sns.color_palette("seismic", len(df_box['year'].unique()))
    sns.boxplot(x='year', y='value', data=df_box, palette=palette_axes0, ax=axes[0])

    # Set the title for the first subplot
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    #Plot second boxplot
    palette_axes1 = sns.color_palette()
    sns.boxplot(x='month', y='value', data=df_box, palette= palette_axes1, ax=axes[1])

    # Set the title for the second subplot
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Adjust layout and show plot
    #plt.tight_layout()
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
