import xml.etree.ElementTree as ET
import pandas as pd
import pdb

starting_year = 2019

def parse_faculty_obj(pub_dict, faculty_file, year_list):

    blacklist_file = open("blacklist")
    blacklist = [line.strip() for line in blacklist_file]

    tree = ET.parse(faculty_file)
    root = tree.getroot()
    total_parsed = 0

    # Only accept entires that contain all the following html tags
    # ee is the link to the paper page
    mandatory_keys = ['title', 'venue', 'year', 'ee']

    # This whole part is very specific to how the DBLP API looks.
    # The XML element "hits" is the one with everything
    for hit in root.find('hits'):

        # Get a unique id for each pub
        pub_id = hit.get('id')
        hit_info = hit[0]

        # Are all needed tags there?
        has_all = True

        # A flat dictionary for one publication
        pub_obj = dict()

        # # Top level dictionary indexed by year.
        year = hit_info.find('year').text

        # Skip anything outside of the desired year range
        if year not in year_list:
            continue

        # Skip unofficial arxiv pubs
        # if hit_info.find('type').text == "Informal Publications":
        #    continue

        # Skip anything in "proceedings of..."
        if hit_info.find("type").text == "Editorship":
            continue

        # If all else fails, skip exact title matches from the blacklist file
        if hit_info.find("title").text in blacklist:
            print("Blacklist hit: " + hit_info.find("title").text)
            continue

        # Skip repeated publication ID (usually from professor co-authorship)
        if pub_id in pub_dict:
            continue

        # Get authors
        if hit_info.find('authors') is None:
            has_all = False

        author_elems = hit_info.find('authors')
        author_list = list()
        for author in author_elems:
            # Fix weird "Ali Mesbah 0001" problem
            # TODO: turn into a regex
            author_name = author.text.replace(" 0001", "")
            author_list.append(author_name)

        pub_obj['authors'] = author_list

        # Get all other keys
        for key in mandatory_keys:

            if hit_info.find(key) is None:
                has_all = False
            
            else:
                # Overwrite "CoRR" to be "ArXiv".
                if key == "venue" and hit_info.find(key).text == "CoRR":
                    pub_obj[key] = "ArXiv"
                else:
                    pub_obj[key] = hit_info.find(key).text

        # Add to the faculty_obj if all keys are there
        if has_all:

            pub_dict[pub_id] = pub_obj
            total_parsed += 1

    return pub_dict, total_parsed


def pub_dict_to_html(pub_dict):

    # convert to pandas for easy sorting
    df = pd.DataFrame.from_dict(pub_dict, orient="index")

    df = df.sort_values(['year', 'venue'], ascending=[False, True])

    file_obj = open("pub_list.html", 'w')

    current_year = 0

    for index, row in df.iterrows():

        # Write a new year header if the year changes
        year = row['year']
        if not year == current_year:
            if not current_year == 0:
                file_obj.write("</ul>\n")

            current_year = year
            file_obj.write("<h3>" + year + "</h3>\n")
            file_obj.write("<ul>\n")

        file_obj.write("<li>\n")

        file_obj.write(
            "<strong>" + row['title'] + "</strong>\n")

        author_string = ", ".join(row['authors'])

        file_obj.write(author_string + ".\n")

        file_obj.write(row['venue'] + "\n")
        file_obj.write(year + ".\n")
        file_obj.write(
            "[<a href=\"" + row['ee'] + "\">link</a>]\n")
        file_obj.write("</li>\n")

    file_obj.write("</ul>\n")


if __name__ == "__main__":

    # Take from the current year, go back 10 years
    year_list = list()
    for i in range(10):
        year_list.append(str(starting_year - i))

    # Only go back 5 years for Margo as of now. Might change later.
    margo_year_list = list()
    for i in range(5):
        margo_year_list.append(str(starting_year - i))

    faculty_files = ['margo.xml', 'andy.xml', 'ivan.xml', 'bill.xml',
                     'alan.xml', 'norm.xml', 'mike.xml']

    # dictionary by year
    pub_dict = dict()
    total_count = 0

    for file in faculty_files:
        faculty_dict, count = parse_faculty_obj(pub_dict, file, year_list)
        print("Parsed " + str(count) + " publications for " + file)
        total_count += count

    print("Parsed " + str(total_count) + " in total.")

    pub_dict_to_html(pub_dict)

    print("Done writing to HTML.")
