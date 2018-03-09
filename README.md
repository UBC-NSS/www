# Lab Website
NSS lab website at UBC

## How to view my fork before pushing to the web?
Review pages with HTML preview using:
https://htmlpreview.github.io/?https://raw.githubusercontent.com/clementfung/www/master/html/index.html

You can also open a local webserver:
`python -m SimpleHTTPServer` 
and go to localhost:8000.

### Photos: Main Slider
These are stored in /files/main-photos  
The default aspect ratio of the photos is 3:2, only because my camera had that setting.  
Add a photo there, and modify the nivoSlider section in index.html to include it in the rotation.

### Photos: Headshots
I use gThumb to crop the image into a square, and then save it in the /files/people-photos directory.  
IMPORTANT: Due to noted security concerns, downsize the image to a maximum size of 300x300.

### Publications: DBLP Query Tool
Just navigate to the /dynamic-dblp directory and call make. 
This will:
- Query DBLP for papers authored by the 6 faculty members here at NSS, and save results into XML
- Parse each of the XML response files into a combined python object, applying some filters
- Write the python object into a pub_list.html file
- Copy the file over the the /html directory

Python dependencies:
- I did everything with python 2.7. TODO: test on python 3.
- pandas
- django (not really important. TODO: remove django)

TODO: Make the filtering easier to manage
