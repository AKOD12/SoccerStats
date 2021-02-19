from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

base_url='https://understat.com/match/'

##For later allowing any match data##
#match_id=str(input('Enter a match ID: '))
#real_url=base_url+match_id

real_url=base_url+'15322'

res=requests.get(real_url)

##web scrape##
sp=BeautifulSoup(res.content, 'lxml')
scripts=sp.findAll('script')
shots_string=scripts[1].string

##stripped symbols##
index_start=shots_string.index("('")+2
index_end=shots_string.index("')")

##string to json##
json_data=shots_string[index_start:index_end]
json_data=json_data.encode('utf8').decode('unicode_escape')

data=json.loads(json_data)

##dataframe creation##
x=[]
y=[]
xg=[]
team=[]
outcome=[]
data_home=data['h']
data_away=data['a']

##home team data##
for i in range(len(data_home)):
    for key in data_home[i]:
        if key=='x':
            x.append(data_home[i][key])
        if key=='y':
            y.append(data_home[i][key])
        if key=='xG':
            xg.append(data_home[i][key])
        if key=='result':
            outcome.append(data_home[i][key])
        if key=='h_team':
            team.append(data_home[i][key])

##away team data##
for i in range(len(data_away)):
    for key in data_away[i]:
        if key=='X':
            x.append(data_away[i][key])
        if key=='Y':
            y.append(data_away[i][key])
        if key=='xG':
            xg.append(data_away[i][key])
        if key=='result':
            outcome.append(data_away[i][key])
        if key=='a_team':
            team.append(data_away[i][key])

col_names=['x','y','Expected Goal Chance','Shot Outcome','Team']
df=pd.DataFrame([x,y,xg,outcome,team], index=col_names)
df=df.T

print(df)