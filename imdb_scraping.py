#!/usr/bin/env python

""" Scraping IMDb Credits

Retrieve listing information for the given IMDb crew link
in the form of a dictionary with the title, role and release year
of each entry.

Example usage: python imdb_scraping.py nm6553571
"""

__author__ = "Aamir Raza"

import sys
import re
from collections import defaultdict
from pprint import pprint

import requests                                # pylint: disable=import-error
from bs4 import BeautifulSoup, SoupStrainer    # pylint: disable=import-error

def process_page(page_id):
    """
    Retrieve listing information for the given IMDb crew link
    in the form of a dictionary with the title, role and release year
    of each entry.

    returns defaultdict in the format:

    {'tt10055546': ['SuperCool',
                            '',
                            '(digital compositor)',
                            'Visual effects']'}
    """

    user_data = defaultdict(list)

    url = 'https://www.imdb.com/name/{}/'.format(page_id)
    print(url)

    page = requests.get(url)

    print("\nRequest Status Code: {}".format(page.status_code))

    # If return code for request is successful
    if page.status_code == 200:

        print("Collecting data...\n")

        # SoupStrainer used to narrow down the page to the filmography section
        filmo_filter = SoupStrainer('div', id="filmography")
        soup = BeautifulSoup(page.text, "html.parser", parse_only=filmo_filter)

        # Use regex to only parse through credit rows
        regex = re.compile('^filmo-row (?:odd|even)')

        # Go through each entry and find the title, year and role
        for entry in soup.find_all('div', class_=regex):

            # Get category for entry
            category = entry.parent.previous_sibling.previous_sibling.find('a')
            category = category.text.strip()

            # Title ID for production
            entry_id = re.search('tt[0-9]{6,10}', entry['id'])
            if entry_id[0] is not None:
                entry_id = entry_id[0]
            else:
                entry_id = "none"

            # Title name for production
            title = entry.find('b')
            entry_title = title.text.strip()

            # Year of production
            year = entry.find('span', class_="year_column")
            entry_year = year.text.strip()

            # Info for entry (sometimes contains role)
            info = entry.find('b').next_sibling.strip()
            if info.endswith('('):
                info = info[:-1].strip()

            # Add each entry to defaultdict
            user_data[entry_id] = [entry_title, entry_year, info, category]

        pprint(user_data)

    return user_data

if __name__ == "__main__":

    # Check if IMDb page id appears valid (not foolproof)
    if (len(sys.argv) > 1 and len(sys.argv[1]) >= 8 and
        str.isdigit(sys.argv[1][2:]) and sys.argv[1][:2] == "nm"):
        process_page(sys.argv[1])
    else:
        print("Not a valid IMDb page")
