import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from mplsoccer.pitch import Pitch

data=pd.read_csv('rbl_aus_test.csv')

fig, ax = plt.subplots(figsize=(13,8.5))

pitch = Pitch(pitch_type='statsbomb', orientation='vertical',
              pitch_color='green', line_color='white', figsize=(13, 8))

pitch.draw(ax=ax)
plt.gca().invert_yaxis()

#plot the points, you can use a for loop to plot the different outcomes if you want
plt.scatter(data['x'],data['y'], s=100,c='#ea6969',alpha=.7)

plt.savefig('test.png', dpi=300,bbox_inches = 'tight',facecolor='#22312b')