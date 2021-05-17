import folium
import requests

def confinement(address):
    # get coordinates
    params = {'q':address,'format':"json"}
    places = requests.get(f'https://nominatim.openstreetmap.org/search?', params =params).json()
    coordinates = places[0]['lat'], places[0]['lon']
    m = folium.Map(coordinates,zoom_start=10)
    folium.Marker(coordinates).add_to(m)
    folium.Circle(radius=10000,location=coordinates).add_to(m)
    return m
