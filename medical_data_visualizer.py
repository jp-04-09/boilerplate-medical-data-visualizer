import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
df.info()
print(df.head())

# 2
df['overweight'] = np.where((df['weight'] / pow(df['height']/100, 2)) > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, np.where(df['cholesterol'] > 1, 1, df['cholesterol']))
df['gluc'] = np.where(df['gluc'] == 1, 0, np.where(df['gluc'] > 1, 1, df['gluc']))

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    print(df_cat)

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable'])['value'].value_counts().reset_index(name='counts')   
    print(df_cat)

    # 7 - 8
    fig = sns.catplot(
                    x='variable',       # x-axis: categorical feature
                    y='counts',
                    hue='value',        # color by value
                    col='cardio',       # create separate plots for each 'cardio' value
                    kind='bar',         # type of plot
                    data=df_cat         # DataFrame to plot
                )

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
