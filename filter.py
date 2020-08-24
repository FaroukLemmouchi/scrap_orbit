import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import datetime
from sys import exit
import xarray as xr


df = pd.read_csv('compiled.csv', sep=',', skipinitialspace=True)

print(df.keys())
df1 = df

todrop = []
for j,i in enumerate(df1.start_overpass) : 
  if datetime.datetime.fromisoformat(i).hour <11 or datetime.datetime.fromisoformat(i).hour > 14:
    df1.iloc[j,5] = ''
    todrop.append(j)

df1 = df1.drop(todrop)

df1 = df1[df['latitude'] > -45 ]
df1 = df1[df1['latitude'] < 55 ]
#df1 = df1[df1['longitude'] > -123 ]
#df1 = df1[df1['longitude'] < 15]
print(df1)


ax= plt.subplot(projection=ccrs.PlateCarree())
plt.scatter(df1.longitude, df1.latitude)
ax.coastlines() 
#plt.show()
plt.savefig('candidates.png')

