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
    year= r.get('http://www.howstat.com/cricket/Statistics/Matches/MatchList_T20.asp?Group='+years+'0101'+years+'1231&Range='+years)
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
    temp['third_innings'] = df1[6].iloc[39:50,:7]
    temp['fourth_innings'] = df1[6].iloc[58:69,:7]
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
        listc =[]
        listd=[]
        run_mean1 =a['first_innings'][2][:7].astype('float64').mean()
        run_mean2 = a['second_innings'][2][:7].astype('float64').mean()
        run_mean3 = a['third_innings'][2][:7].astype('float64').mean()
        run_mean4 = a['fourth_innings'][2][:7].astype('float64').mean()
        run_mean = (run_mean1+run_mean2+run_mean3+run_mean4)/4
        for element in a['first_innings'][2]:
            lista.append(float("{:.2f}".format(float(element)/mean)))
        for element in a['second_innings'][2]:
            listb.append(float("{:.2f}".format(float(element)/mean)))
        for element in a['third_innings'][2]:
            listc.append(float("{:.2f}".format(float(element)/mean)))
        for element in a['fourth_innings'][2]:
            listd.append(float("{:.2f}".format(float(element)/mean)))
        a['first_innings']['normalised'] = lista
        a['second_innings']['normalised'] = listb
        a['third_innings']['normalised'] = listb
        a['fourth_innings']['normalised'] = listb
    except:
        pass
    
diction ={}

for a in odi_data:
    try:
        temp1 = a['first_innings']
        temp2 = a['second_innings']
        temp3 = a['third_innings']
        temp4 = a['fourth_innings']
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
                
        for b in range(39,39+len(temp3)):
            if(temp3[0][b] not in diction.keys()):
                diction[temp3[0][b]] = []
                diction[temp3[0][b]].append(int(temp3['normalised'][b]))
            else:
                diction[temp3[0][b]].append(int(temp3['normalised'][b]))
        for b in range(58,58+len(temp4)):
            if(temp4[0][b] not in diction.keys()):
                diction[temp4[0][b]] = []
                diction[temp4[0][b]].append(int(temp4['normalised'][b]))
            else:
                diction[temp4[0][b]].append(int(temp4['normalised'][b]))
  
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

test_df = pd.DataFrame(list(zip(player_list, average_list,count)), 
               columns =['Player Name', 'Average','Matches']) 
    

sub_test_df = test_df[test_df['Matches']>50]

    
top10 = sub_test_df.nlargest(20, ['Average']) 

test_df.to_csv('/Users/shray/Desktop/ipl/new_completetest.csv')












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