# Aria Nagai IW
import numpy as np
from numpy import genfromtxt
import csv
import pandas as pd
import geopandas

# low birth weight dataframe
def lbw_total():
   lwdf = pd.read_csv("Datasets/lowweight_by_race.csv")

   path_to_data = geopandas.datasets.get_path("nybb")
   gdf = geopandas.read_file(path_to_data)

   # by race 
   race_df = pd.merge(gdf,lwdf, on='BoroCode')

   # total lbw
   total_births_df = pd.read_csv('Datasets/lowweight_total.csv')
   total_lbw_gdf = pd.merge(gdf,total_births_df,on='BoroCode')
   total_lbw_gdf['percentage']=total_lbw_gdf['percentage']*100

  

   return lwdf, gdf, race_df, total_lbw_gdf

def lbw_total_race(gdf):
   # total lbw by race
   total_allyears_lbw_df = pd.read_csv('Datasets/total_lbw_race_allyears.csv')
   total_allyears_lbw_gdf = pd.merge(gdf,total_allyears_lbw_df,on='BoroCode')
   total_allyears_lbw_gdf['percentage']=total_allyears_lbw_gdf['percentage']*100

   # asian
   allyears_a = total_allyears_lbw_gdf[total_allyears_lbw_gdf['race']=='Asian']

   # aa
   allyears_aa = total_allyears_lbw_gdf[total_allyears_lbw_gdf['race']=='Black or African American']

   # white
   allyears_w = total_allyears_lbw_gdf[total_allyears_lbw_gdf['race']=='White']

   return allyears_a, allyears_aa, allyears_w


# def lbw_per_year(total_lbw_gdf, race_df, year):
#    # 2016 df
#    race_df.loc[race_df["500-2500g births"]=="suppressed","500-2500g births"] = 0
#    race_year_df = race_df[race_df['Year']==year]
#    race_year_df['percentage'] = race_year_df['percentage']*100
#    lbw_year = total_lbw_gdf[total_lbw_gdf['year']==year]
#    lbw_year_A_total=pd.read_csv('Datasets/asian_lbw_2016_total.csv')
#    lbw_year_A_total=pd.merge(gdf,lbw_2016_A_total)
#    lbw_year_AA_total=pd.read_csv('Datasets/aa_lbw_2016_total.csv')
#    lbw_year_AA_total=pd.merge(gdf,lbw_2016_AA_total)
#    lbw_year_AA_total['Percentage']=lbw_2016_AA_total['Percentage']*100
#    lbw_year_W_total=pd.read_csv('Datasets/white_lbw_2016_total.csv')
#    lbw_year_W_total=pd.merge(gdf,lbw_2016_W_total)
#    lbw_year_W_total['Percentage']=lbw_2016_W_total['Percentage']*100

#    # 2017 
#    lbw_2017 = total_lbw_gdf[total_lbw_gdf['year']==2017]