# Map_LR_2
# MAP GENERATOR
### !!!NOTE!!!
#### not all locations are being used due to time consuming data parsing. if wanded all locations can be extracted properly in longer time. processed database consists of about 50,000 locations.
### PROGRAM USE

###### This program returns generated map that reassembles the 10 closest movies that were filmed on certain year...
####
- ##### First module:
  - Using [locations.txt](https://cms.ucu.edu.ua/pluginfile.php/158762/mod_assign/introattachment/0/locations.list?forcedownload=1) database.    
  - Goes through file and gets cities latitude and longatude based on their location name (ex. China: 37.0902, 95.7129)
  - Filters citie's data into files based on the year the filme/serial was recorded.
  - Uses the package manager [pip](https://pip.pypa.io/en/stable/) to install geopy.
```bash
pip install geopy
```
- ##### Second module: 
  - Goes throught file with entered movie year and calculates all distances from my positon to all other.
  - Calculates the number of same movies.
  - Sorts all distances and takes top 10 closes to my location movies by their distance.

- ##### Main Module
  - After you can select the year of filmed movies that are to be shown and enter your location.
  - At the end hit ENTER.

### HTML
- ##### Tags
  - script src=... - If we want to refer to .js file that was previously saved before on website.
  - link rel... - Specifies the way current documents are linked.
  - a href=... - Specifies the URL of the page the link follows to.
  - style - This tag is used to define the style of the page.
  - meta name=... - Provides metadata for the URL page.
  - head - Defines the title for the URL page.
  - body - Defines URL's document body.
  - div class=... - Creates a class and makes all elements with the same class name to secrtain style.
  - div id=... - The ID of the element of the class.


### INFORMATION
##### - About the map
####
###### Generated map shows us where the movies of a cetain year were shot. Also places a "marker" on that position. Also colors the "marker" the color based on how many of the same movies were filmed on the same location.
######  For additionl use there is also drawn distances from the point our location is to each "marker". And provides each line with a distance to the "marker".
####
### EXAMPLE
```
 >>> python main.py
Please enter a year you would like to have a map for: 2015
Please enter your location (format: lat, long): 49.83826, 24.02324
Map is generating...
Please wait...
Finished. Please have look at the map: map.html
```

#### Image
![Alt text](https://github.com/SlavkoPrytula/Map_LR_2/blob/master/Screenshot_20200218_145424-1.png?raw=true "Title")

```
 >>> python main.py
Please enter a year you would like to have a map for: 1995
Please enter your location (format: lat, long): 37.0902, 95.7129
Map is generating...
Please wait...
Finished. Please have look at the map: map.html
```

#### Image
![Alt text](https://github.com/SlavkoPrytula/Map_LR_2/blob/master/Screenshot_20200218_153418.png?raw=true "Title")



