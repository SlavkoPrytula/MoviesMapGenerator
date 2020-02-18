import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from folium.features import DivIcon

geolocator = Nominatim(user_agent='myapplication')


def find_locations(year, lat_start, lon_start):

    """
    (int)(int, int) -> (map.html)

    This function returns generated map that reassembles
    the closest movies that were filmed on certain year.

    Also puts markers in those positions and changes
    their color depending on how much series of the
    movie or serial were filmed on the same location.

    """

    distances_dict = {}
    latitude_start = lat_start
    longatude_start = lon_start
    start_point = (latitude_start, longatude_start)
    m = folium.Map(location=[latitude_start, longatude_start], zoom_start=4.2, tiles='OpenStreetMap')

    directory = "Years_Updated"

    marker = folium.Marker([latitude_start, longatude_start],
                           popup="<b><strong>{}</strong></b>".format("My_location"),
                           icon=folium.Icon(color="red")).add_to(m)

    # Create layer:
    lines_group = folium.FeatureGroup(name="Distances").add_to(m)

    f = open("{}/{}.txt".format(directory, year), "r")
    films = []
    for line in f.readlines():
        line = line.strip().split("\t")
        # print(line)
        latitude = line[-2]
        longatude = line[-1]
        new_point = (latitude, longatude)
        distance = geodesic(start_point, new_point).km

        film_count = 1
        film_name = line[0].split("'")[1]
        # print(film_name)
        films.append(film_name)

        distances_dict.update({distance: (film_name, films.count(film_name), latitude, longatude)})

    distances_dict = {key: distances_dict[key] for key in sorted(distances_dict.keys())}
    # print(distances_dict)
    # print(films)

    count = 0
    for item in distances_dict:
        if count <= 9:
            lat = distances_dict[item][-2]
            lon = distances_dict[item][-1]
            dis = item
            name = str(distances_dict[item][0].split(" (")[0] + "\n\n" + "Files found: " + str(distances_dict[item][1]))
            color_item = distances_dict[item][1]
            color = "green"

            # Place marker:
            if color_item in range(0, 3):
                color = "green"
            elif color_item in range(3, 7):
                color = "orange"
            elif color_item in range(7, 10):
                color = "red"
            else:
                color = "darkblue"

            marker = folium.Marker([lat, lon],
                                   popup="<b><strong>{}</strong></b>".format("Name: \n" + name),
                                   icon=folium.Icon(color=color, icon="film outline")).add_to(m)

            text_lat = (float(lat) + float(latitude_start)) / 2
            text_lon = (float(lon) + float(longatude_start)) / 2
            text = folium.map.Marker(
                [text_lat, text_lon],
                icon=DivIcon(
                    icon_size=(150, 36),
                    icon_anchor=(0, 0),
                    html='<b><div style="font-size: 10pt">{}</div></b>'.format(str(round(dis)) + " km"),
                )
            ).add_to(m)

            coordinates = [[latitude_start, longatude_start], [lat, lon]]
            line = folium.PolyLine(locations=coordinates).add_to(m)

            # Add distance to the layer:
            lines_group.add_child(text)
            lines_group.add_child(line)

            # Save:
            m.save('map.html')
            count += 1

    folium.LayerControl().add_to(m)
    m.save('map.html')
