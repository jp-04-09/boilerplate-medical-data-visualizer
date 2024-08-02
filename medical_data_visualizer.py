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
df['cholesterol'] = np.where((df['cholesterol'] == 1), 0, 1)
df['gluc'] = np.where((df['gluc'] == 1), 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    print(df_cat)

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable'])['value'].value_counts().reset_index(name='total')   
    print(df_cat)

    # 7 
    plt.figure()
    catplot = sns.catplot(
                    x='variable',       # x-axis: categorical feature
                    y='total',
                    hue='value',        # color by value
                    col='cardio',       # create separate plots for each 'cardio' value
                    kind='bar',         # type of plot
                    data=df_cat         # DataFrame to plot
                )

    # 8
    fig = catplot.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat =  df[(df['ap_lo'] <= df['ap_hi']) &
                  (df['height'] >= df['height'].quantile(0.025)) & 
                  (df['height'] <= df['height'].quantile(0.975)) &
                  (df['weight'] >= df['weight'].quantile(0.025)) & 
                  (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
