import LR_2_2_building_map

def read_data(y, la, lo):
    print('''Map is generating... \nPlease wait...''')
    LR_2_2_building_map.find_locations(y, la, lo)
    print('Finished. Please have look at the map: map.html')

    


if __name__ == "__main__":
    year = str(input("Please enter a year you would like to have a map for: "))
    location = str(input("Please enter your location (format: lat, long): "))
    locations_dict = location.split(",")
    lat = float(locations_dict[0])
    lon = float(locations_dict[1])

    if len(locations_dict) != 2:
        print("Error")
    elif len(year) != 4 and int(year) not in range(1000, 3000):
        print("Error")
    else:
        read_data(year, lat, lon)

