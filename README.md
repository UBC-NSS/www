# Lab Website
NSS lab website at UBC

## How to view my fork before pushing to the web?
Review pages with HTML preview using:
https://htmlpreview.github.io/?https://raw.githubusercontent.com/UBC-NSS/www/master/html/index.html

You can also open a local webserver:
`python -m SimpleHTTPServer` 
and go to localhost:8000.  
This is also given in `deploy-local-website-8000.sh` for super ease.

### Photos: Main Slider
These are stored in /files/main-photos  
The default aspect ratio of the photos is 3:2, only because my camera had that setting.  
Add a photo there, and modify the nivoSlider section in index.html to include it in the rotation.

### Photos: Headshots
All the original shots are stored in /files/people-photos/unedited  
I use gThumb to crop the image into a square, and then save it in the /files/people-photos directory.  

### Publications: DBLP Query Tool
Just navigate to the `/dynamic-dblp` directory and call `make`. 
This will:
- Query DBLP for papers authored by the 6 faculty members here at NSS, and save results into XML
- Parse each of the XML response files into a combined python object, applying some filters
- Filter out a pub if the title matches exactly in the `blacklist` file.
- Write the python object into a `pub_list.html` file
- Copy the file over the the `/html` directory

TODO: how to incorporate Margo's future pubs easily?

Python dependencies:
- I did everything with python 2.7. TODO: test on python 3.
- pandas


