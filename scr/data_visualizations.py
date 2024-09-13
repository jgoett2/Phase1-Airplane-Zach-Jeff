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
    
    x = pd.DataFrame([(x, float(ave_fraction.loc[x].iloc[0])) for x in top_five]).sort_values(by=1)

    sns.barplot(data=x, x=0, y = 1, ax=ax).set(xlabel='Make_Model', ylabel=stat, title=word+" Models")


def performance_make_damage(df, stat):
  fig, ax = plt.subplots(1,2,figsize=[14,5])
  df_substantial = df[df["Aircraft.damage"] == "Substantial"]
  df_destroyed = df[df["Aircraft.damage"] == "Destroyed"]

  order = df_substantial[["Make",stat]].groupby("Make").mean().sort_values(by=stat, ascending=False).index
  sns.barplot(data=df_substantial, x='Make', y = stat, order=order, ax=ax[0]).set(title=stat + " vs. Make for Substantial Damage")

  order = df_destroyed[["Make",stat]].groupby("Make").mean().sort_values(by=stat, ascending=False).index
  sns.barplot(data=df_destroyed, x='Make', y = stat, order=order, ax=ax[1]).set(title=stat + " vs. Make for Destroyed Damage")

  fig.savefig("Images/" + stat + "Make")


def performance_phase(df, stat):
  fig, ax = plt.subplots(figsize= (12,6))

  phases_flight = df["Broad.phase.of.flight"].value_counts().drop(["Unknown", "Other"]).index
  df_phases = df[df["Broad.phase.of.flight"].map(lambda x: x in phases_flight)]

  order = df_phases[["Broad.phase.of.flight",stat]].groupby("Broad.phase.of.flight").mean().sort_values(by=stat,ascending=False).index

  sns.barplot(data=df_phases, y='Broad.phase.of.flight', x = stat, order=order, ax=ax).set(title=stat + " vs. Phase of Flight", 
                                                                                   xlabel=stat, ylabel="Phase of flight")

  #ax.tick_params(labelsize=12)
  #ax.set_xlabel(stat, fontweight = 'bold', fontsize=14)
  #ax.set_ylabel('Phase of flight', fontweight = 'bold', fontsize=14)

  fig.savefig("Images/PhaseOfFlight" + stat)



def best_models(df):
   dfPC = df[(df['Make'] == 'Cessna') | (df['Make'] == 'Piper') ]
   dfPC = dfPC[dfPC["Aircraft.damage"] == "Destroyed"]
   dfPCd = dfPC.groupby("Make_Model").count().sort_values(by="Event.Id",ascending=False)
   top_5 = dfPCd.index[:5]
   ave_frac = dfPC[["Make_Model","Fraction_uninjured"]].groupby("Make_Model").mean()
   xy = pd.DataFrame([(x,float(ave_frac.loc[x])) for x in top_5]).sort_values(by=1)
   fig, ax = plt.subplots(figsize = (10,7))

   sns.barplot(data=xy, x=0, y=1).set(xlabel="Make_Model", ylabel="Fraction Uninjured", title="Destroyed per Make_Model in Ininjured")
   #ax.set_ylabel("Fraction Uninjured")
   #ax.set_title("Destroyed per Make_Model in Uninjured")

   fig.savefig("Images/Make_ModelDestroyedUninjured")