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
    
 returns defaultdict in the format:
    
    {'tt10055546': ['SuperCool',
                            '',
                            '(digital compositor)',
                            'Visual effects']'}
