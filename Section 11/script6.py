import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start = 5,tiles='Stamen Terrain')

def color(elev):
    minimum = int(min(df['ELEV']))
    step = int(((1/3)*(max(df["ELEV"]) - min(df["ELEV"]))))
    if elev in range(minimum, minimum + step) :
        col = 'green'
    elif elev in range(minimum + step,minimum + (2*step)):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.add_child(folium.Marker(location=[lat, lon],popup=name,icon = folium.Icon(color=color(elev),icon_color='blue')))

map.save(outfile="test.html")
