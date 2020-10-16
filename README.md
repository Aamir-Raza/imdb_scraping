Module imdb_scraping
====================
Scraping IMDb Credits

Retrieve listing information for the given IMDb crew link
in the form of a dictionary with the title, role and release year
of each entry.

Example usage: 

    python imdb_scraping.py nm6553571

Functions
---------

    
`process_page(page_id)`
:   Retrieve listing information for the given IMDb crew link
    in the form of a dictionary with the title, role and release year
    of each entry.   
    
returns defaultdict in the format *title id: Name, Year, Info, Category*
    
    'tt2802850': ['Fargo',
                           '2017',
                           '(TV Series) (digital compositor - 1 episode)',
                           'Visual effects'],
    'tt3065204': ['The Conjuring 2',
                           '2016',
                           '(digital compositor)',
                           'Visual effects']
