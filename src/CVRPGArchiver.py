import time
import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import sys

import logger

def save_image (page_soup,download_location):
    """
    Downloads the image from the current page.
    Saves it into the folder for the current year/count.
    Hundreds are used where a year is not readily available.
    """
    # Get the div with the image tag
    img_wrapper = str(page_soup.find("div", {"id":"comic-image"}))

    # Get the actual image tag
    re_pattern = '<img src=".*"/>'
    img_node = re.search(re_pattern, img_wrapper).group()
    logger.debug_print("img_node", img_node)

    # Use the image tag to calculate the location of the image file.
    # Strip leading and trailing extra characters from the img tag.
    img_source = "https://www.cvrpg.com/" + img_node[11:-3]
    logger.debug_print("img_source", img_source)

    # Use the image file to calculate the file name for downloading.
    re_pattern = '/comics/[a-z]*[0-9]*\.gif'
    img_name = re.search(re_pattern,img_source)
    if None is img_name:
        print ("keep working on your regex")
        sys.exit()
    else:
        img_name = img_name.group()[8:]
    logger.debug_print("img_name", img_name)

    # Assemble the fully qualified path for the downloaded image.
    full_download_path = download_location + '/' + img_name
    logger.debug_print("full_download_path", full_download_path)

    img_data = requests.get(img_source).content
    with open(full_download_path, 'wb') as handler:
        handler.write(img_data)

def get_next_page (page_soup):
    """
    Takes in the page being currently processed and returns the URL in string
    form.  Returns None if not found.
    """

    #Pull the relevant element out of the page
    fragment = str(page_soup.find("li", {"class":"comic-next"}))

    #Extract the URL fragment from the element
    re_pattern = '/.*"'

    next_fragment = re.search(re_pattern, fragment).group()[1:-1]
    logger.debug_print ("next_fragment", next_fragment)

    # Strip extra characters
    next_url = "https://www.cvrpg.com/" + next_fragment
    logger.debug_print("next_url", next_url)

    return next_url

def archive_comic(download_location):
    """
    Pulls down every comic image from the webcomic.
    download_location: where to stick the downloaded images.
    """

    # Starting comic
    current_url = "https://www.cvrpg.com/archive/comic/2002/01/01"

    # Stops the run after a few reps to keep from downloading the entire comic
    # unintentionally during testing.
    repetitions = 3

    while None is not current_url and 0 < repetitions:
        logger.debug_print("Number remaining", repetitions)

        with urllib.request.urlopen(current_url) as response:
            html = response.read()

        page_soup = BeautifulSoup(str(html), 'html.parser')

        save_image(page_soup, download_location)
        current_url = get_next_page(page_soup)

        repetitions -= 1

        # Pause for a moment to keep the load on the server low.
        time.sleep(5)

def main():
    download_to = "downloads"
    
    archive_comic(download_to)
    
if "__main__" == __name__: 
    main()