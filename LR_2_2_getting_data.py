from geopy.geocoders import Nominatim
import os
import time

geolocator = Nominatim(user_agent='myapplication')


def get_locations():

    """

    This program goes through locations.txt and gets
    location from each line.
    Then gets latitude and longitude from the the city.
    After writes the name of the fim and its location to
    a file with corresponding year. (ex. "2015.txt")

    """

    directory = "Years_Updated"
    last_name = ""
    last_loc = ""
    last_year = ""
    last_latitude = 0
    last_longatude = 0

    f = open("locations.txt", "r")

    for line in f.readlines():
        line = line.strip("\n").split("\t")
        if "(" in line[-1]:
            line.remove(line[-1])

        # Get into files:
        # set default (just in case):
        year = ""
        for i in line[0].split(" ("):
            try:
                # print(i)
                item = i[:4]
                # print(item)
                if item.isdigit():
                    year = item
                elif item == "????":
                    year = "????"
            except IndexError:
                pass

        complete_name = os.path.join(directory, year + ".txt")
        file = open(complete_name, "a")

        movie_name = line[0].split(" (")[0]
        movie_location = line[-1]

        latitude = 0
        longatude = 0

        try:
            if last_year != year or last_loc != movie_location:
                location = geolocator.geocode(line[-1])

                latitude = location.latitude
                longatude = location.longitude

                last_name = movie_name
                last_loc = movie_location

                print(line, latitude, longatude, "c")

            elif last_year == year and movie_location == last_loc:
                latitude = last_latitude
                longatude = last_longatude
                last_name = movie_name
                last_loc = movie_location
                print(line, latitude, longatude, "b")

        except:
            try:
                if last_year != year or last_loc != movie_location:
                    new_line_coma_split = line[-1].split(",")
                    new_name = new_line_coma_split[-3] + new_line_coma_split[-2] + new_line_coma_split[-1]
                    location = geolocator.geocode(new_name)
                    latitude = location.latitude
                    longatude = location.longitude
                    last_name = movie_name
                    last_loc = movie_location
                    print(line, latitude, longatude)
                elif last_year == year and movie_location == last_loc:
                    latitude = last_latitude
                    longatude = last_longatude
                    last_name = movie_name
                    last_loc = movie_location
                    print(line, latitude, longatude, "a")

            except:
                try:
                    if last_year != year or last_loc != movie_location:
                        new_line_coma_split = line[-1].split(",")
                        new_name = new_line_coma_split[-1]
                        location = geolocator.geocode(new_name)
                        latitude = location.latitude
                        longatude = location.longitude
                        last_name = movie_name
                        last_loc = movie_location
                        print(line, latitude, longatude)
                    elif last_year == year and movie_location == last_loc:
                        latitude = last_latitude
                        longatude = last_longatude
                        last_name = movie_name
                        last_loc = movie_location
                        print(line, latitude, longatude, "a")

                except:
                    last_name = movie_name
                    last_loc = movie_location
                    print(line, latitude, longatude, "here")

        last_year = year
        last_latitude = latitude
        last_longatude = longatude

        # Write to the file:
        if latitude != 0 and longatude != 0:
            file.write(str(line) + "\t" + str(latitude) + "\t" + str(longatude) + "\n")
        else:
            time.sleep(300)


get_locations()
