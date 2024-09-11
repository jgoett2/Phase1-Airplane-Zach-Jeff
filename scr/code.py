import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def hi(df, word, stat, ax):
    dfB = df[df['Make'] == word]
    GB = dfB.groupby('Make_Model').count().sort_values(by='Event.Id', ascending=False)
    top_five = GB.index[:5]
    top_five
    ave_fraction = dfB[["Make_Model",stat]].groupby("Make_Model").mean()
    ave_fraction
    
    x = pd.DataFrame([(x, float(ave_fraction.loc[x])) for x in top_five]).sort_values(by=1)
    
    ax.set_xlabel('Make_Model')
    ax.set_ylabel(stat)
    ax.set_title(word+' Models')

    return sns.barplot(data=x, x=0, y = 1, ax=ax)