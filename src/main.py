"""
Takes in the first page in a webcomic archive, then goes next page by next page,
downloading the image that makes up the comic.  Where the image is not properly
formatted for browsing, prepends either the page number or the publication date
of the comic to the image file.

Designed for use with single-image comics.

Start with the webcomic Schlock Mercenary.
"""

import time.sleep
import urllib.request

def get_next_page (page_url):
    """
    Takes in the page being currently processed and returns the URL in string
    form.  Returns None if not found.
    """

    #Pull the next page out of the html
    next_url = page_url
    next_url = None
    return next_url

def save_image (page_url,download_location):

    """
    Downloads the image from the current page.
    Saves it into the folder for the current year.
    """
    download_location = None


def archive_comic(starting_url):

    download_location = "./downloads"
    current_url = starting_url

    while None is not current_url:
        #TODO: refactor save_image and current_url to use the HTML pulled from
        # urllib so you only have to pull the HTML once.

        with urllib.request.urlopen(current_url) as response:
            html = response.read()

        save_image(html, download_location)
        current_url = get_next_page(html)
        time.sleep(10)

archive_comic ("https://www.schlockmercenary.com/2000-06-12")
