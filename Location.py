import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

data = {
    'City': ['Tehran', 'Mashhad', 'Isfahan', 'Karaj', 'Shiraz', 'Tabriz', 'Qom', 'Ahvaz', 'Kermanshah', 'Urmia'],
    'Population': [8846782, 3074847, 1963119, 1963360, 1565572, 1598463, 1241526, 1184785, 946651, 736224],
    'Latitude': [35.6892, 36.2605, 32.6613, 35.8400, 29.5918, 38.0667, 34.6401, 31.3183, 34.3142, 37.5553],
    'Longitude': [51.3890, 59.6168, 51.6804, 50.9391, 52.5836, 46.2919, 50.8764, 48.6706, 47.0650, 45.0728]
}

df = pd.DataFrame(data)
# print(df)

plt.figure(figsize=(12, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=32, lon_0=54,
            llcrnrlon=44, llcrnrlat=25, urcrnrlon=63, urcrnrlat=40)

m.shadedrelief()
m.drawcoastlines()
m.drawcountries()
m.drawparallels(range(25, 41, 5), labels=[1,0,0,0])
m.drawmeridians(range(44, 64, 5), labels=[0,0,0,1])

x, y = m(df['Longitude'].values, df['Latitude'].values)

m.scatter(x, y, s=df['Population'] / 1000, c='red', alpha=0.5, edgecolors="w", linewidth=2,zorder=5)

for i in range(df.shape[0]):
    plt.text(x[i], y[i], df['City'][i], fontsize=12, ha='right', color='blue')

plt.title('Most Populated Cities in Iran')

plt.show()

