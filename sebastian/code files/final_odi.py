#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 05:00:22 2020

@author: shray
"""

import pandas as pd
import requests as r
from bs4 import BeautifulSoup as bs

year_list = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

match_list =[]

for years in year_list:
    year= r.get('http://www.howstat.com/cricket/Statistics/Matches/MatchList_ODI.asp?Group='+years+'0101'+years+'1231&Range='+years)
    soup = bs(str(year.text),'lxml')

    h = soup.find('table',attrs={'class':'TableLined'})

    soup2 = bs(str(h),'lxml')
    
    matches = soup2.findAll('tr')

    for a in matches:
        try:
            match_list.append(a.findAll('a')[2]['href'])
        except:
            pass

odi_data =[]

for a in match_list:
    temp ={}
    html = r.get('http://www.howstat.com/cricket/Statistics/Matches/'+a)
    hello = str(html.text)
    df1 = pd.read_html(str(html.text))
    temp['match'] = a
    temp['first_innings'] = df1[6].iloc[1:12,:7]
    temp['second_innings'] = df1[6].iloc[20:31,:7]
    odi_data.append(temp)
 
unique_players = []

for a in odi_data:
    for b in list(a['first_innings'][0]):
        if(b not in unique_players):
            unique_players.append(b)
    for b in list(a['second_innings'][0]):
        if(b not in unique_players):
            unique_players.append(b)

for a in odi_data:
    try:
    
        lista=[]
        listb =[]
        run_mean1 =a['first_innings'][2][:7].astype('float64').mean()
        run_mean2 = a['second_innings'][2][:7].astype('float64').mean()
        run_mean = (run_mean1+run_mean2)/2
        for element in a['first_innings'][2]:
            lista.append(float("{:.2f}".format(float(element)/mean)))
        for element in a['second_innings'][2]:
            listb.append(float("{:.2f}".format(float(element)/mean)))
        a['first_innings']['normalised'] = lista
        a['second_innings']['normalised'] = listb
    except:
        pass
    
diction ={}

for a in odi_data:
    try:
        temp1 = a['first_innings']
        temp2 = a['second_innings']
        for b in range(1,len(temp1)+1):
            if(temp1[0][b] not in diction.keys()):
                diction[temp1[0][b]] = []
                diction[temp1[0][b]].append(int(temp1['normalised'][b]))
            else:
                diction[temp1[0][b]].append(int(temp1['normalised'][b]))
        for b in range(20,20+len(temp2)):
            if(temp2[0][b] not in diction.keys()):
                diction[temp2[0][b]] = []
                diction[temp2[0][b]].append(int(temp2['normalised'][b]))
            else:
                diction[temp2[0][b]].append(int(temp2['normalised'][b]))
    except:
        pass
        
player_list =[]
average_list =[]
count =[]

for key,value in diction.items():
    try:
        player_list.append(key)
        average_list.append(sum(value)/len(value)*100)
        count.append(len(value))
    except:
        pass


sum(diction['V Kohli'])/len(diction['V Kohli'])

odi_df

odi_df = pd.DataFrame(list(zip(player_list, average_list,count)), 
               columns =['Player Name', 'Average','Matches']) 
    

sub_odi_df = odi_df[odi_df['Matches']>30]

    
top10 = sub_odi_df.nlargest(20, ['Average']) 

top10.to_csv('/Users/shray/Desktop/ipl/new_top20odi_min50matches.csv')



dfs= odi_data[574]['first_innings']

dfs[2].astype('float64').mean()

dfs[2][:7].mean()


dfs[2][:6]

dfs['hello']
lista=[]


for element in dfs[2]:
    
    mean = dfs[2].astype('float64').mean()
    lista.append(float("{:.2f}".format(float(element)/mean)))    
    
    
for index, row in dfs.iterrows():
    print(row[2][:7])
    
    mean = dfs[2].astype('float64').mean()
    lista.append(float("{:.2f}".format(float(row[2])/mean)))
    
    
    
list(odi_data[574]['first_innings'][0])