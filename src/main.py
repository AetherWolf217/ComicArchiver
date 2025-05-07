"""
Takes in the first page in a webcomic archive, then goes next page by next page,
downloading the image that makes up the comic.  Where the image is not properly
formatted for browsing, prepends either the page number or the publication date
of the comic to the image file.

Designed for use with single-image comics.

Start with the webcomic Schlock Mercenary.
"""

import SchlockArchiver
import CVRPGArchiver

def main():
    """
    Test function for the webcomic archiver.
    """
    download_to = "downloads"

    SchlockArchiver.archive_comic(download_to)
    CVRPGArchiver.archive_comic(download_to)

main()
