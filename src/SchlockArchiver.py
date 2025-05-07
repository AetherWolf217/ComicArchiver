import time
import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import sys

import logger

class SchlockArchiver:
    def save_image (page_soup,download_location):
        """
        Downloads the image from the current page.
        Saves it into the folder for the current year/count.
        Hundreds are used where a year is not readily available.
        """
        # Get the image tag
        img_wrapper = str(page_soup.find("div", {"class":"strip-image-wrapper"}))

        # Get the source location
        re_pattern = '<img src=".*"/>'
        img_node = re.search(re_pattern, img_wrapper).group()
        #logger.debug_print("img_node", img_node)

        img_source = "https://www.schlockmercenary.com" + img_node[10:-3]
        logger.debug_print("img_source", img_source)

        re_pattern = '/schlock.*jpg'
        img_name = re.search(re_pattern,img_source)
        if None is img_name:
            print ("keep working on your regex")
            sys.exit()
        else:
            img_name = img_name.group()[1:]
        logger.debug_print("img_name", img_name)

        #Hold off on doing the folders at first.
        #re_pattern = '/schlock.*jpg'
        #download_year = re.search(re_pattern,img_node).group()[8:-8]

        img_data = requests.get(img_source).content
        with open(download_location + '/' + img_name, 'wb') as handler:
            handler.write(img_data)

    def get_next_page (page_soup):
        """
        Takes in the page being currently processed and returns the URL in string
        form.  Returns None if not found.
        """

        #Pull the relevant element out of the page
        fragment = str(page_soup.find("a", {"class":"next-strip"}))

        #Extract the URL fragment from the element
        re_pattern = '/.*"'

        next_fragment = re.search(re_pattern, fragment).group()[1:-1]
        logger.debug_print ("next_fragment", next_fragment)

        # Strip extra characters
        next_url = "https://schlockmercenary.com/" + next_fragment
        logger.debug_print("next_url", next_url)

        return next_url

    def archive_comic(download_location):
        """
        Pulls down every comic image from a webcomic given the start of the archive.
        starting_url: the URL to start downloading from
        download_location: where to stick the downloaded images.
        """

        current_url = "https://www.schlockmercenary.com/2000-06-12"

        # Stops the run after a few reps to keep from downloading the entire comic
        # unintentionally during testing.
        repetitions = 3

        while None is not current_url and 0 < repetitions:
            logger.debug_print("Number remaining", repetitions)

            with urllib.request.urlopen(current_url) as response:
                html = response.read()

            page_soup = BeautifulSoup(str(html), 'html.parser')

            SchlockArchiver.save_image(page_soup, download_location)
            current_url = SchlockArchiver.get_next_page(page_soup)

            repetitions -= 1

            # Pause for a moment to keep the load on the server low.
            time.sleep(5)

def main():
    download_to = "downloads"
    
    SchlockArchiver.archive_comic(download_to)
    
if "__main__" == __name__: 
    main()