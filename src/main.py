"""
Takes in the first page in a webcomic archive, then goes next page by next page,
downloading the image that makes up the comic.  Where the image is not properly
formatted for browsing, prepends either the page number or the publication date
of the comic to the image file.

Designed for use with single-image comics.

Start with the webcomic Schlock Mercenary.
"""

import time
import urllib.request
from bs4 import BeautifulSoup

def save_image (page_soup,download_location):
    """
    Downloads the image from the current page.
    Saves it into the folder for the current year/count.
    Hundreds are used where a year is not readily available.
    """
    if debug:
        print ("***Saving Image from: " + str(page_soup)[:100] + " to: " \
           + str(download_location))
    
    


def get_next_page (page_soup):
    """
    Takes in the page being currently processed and returns the URL in string
    form.  Returns None if not found.
    """

    if debug:
        print ("***Getting next page from: " + str(page_soup)[:100])

    #TODO Pull the next page out of the html
    next_url = page_soup
    next_url = None
    return next_url

def archive_comic(starting_url, download_location):
    """
    Pulls down every comic image from a webcomic given the start of the archive.
    starting_url: the URL to start downloading from
    download_location: where to stick the downloaded images.
    """

    current_url = starting_url

    # Stops the run after a few reps to keep from downloading the entire comic
    # unintentionally during testing.
    repetitions = 3

    while None is not current_url and 0 < repetitions:

        with urllib.request.urlopen(current_url) as response:
            html = response.read()

        page_soup = BeautifulSoup(html)
        
        save_image(page_soup, download_location)
        current_url = get_next_page(page_soup)

        repetitions -= 1

        # Pause for a moment to keep the load on the server low.
        time.sleep(5)

def main():
    """
    Test function for the webcomic archiver.
    """
    download_to = "../downloads"
    archive_comic ("https://www.schlockmercenary.com/2000-06-12", download_to)

debug = True
main()
