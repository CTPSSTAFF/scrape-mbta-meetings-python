# scrape-mbta-meetings-python
Scrape data from MBTA meetings website using Python's BeautifulSoup package

This is a companion repository to Steven Andrews' [scrape_mbta_meetings](https://github.com/CTPSSTAFF/scrape_mbta_meetings) repo 
illustrating how data can be 'scraped' from the MBTA meetings website in Python using 
the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) package.

As is the case with the example written in R (and indeed pretty much _any_ screen-scraping program), this script relies upon knowledge of
the structure of the HTML produced by the website in quesiton. __If the page structure changes, the script will no longer work.__

In general, some familiarity with HTML and CSS is required in order to write an HTML 'screen-scraper.' 

The organization and structure of a page to be scraped can be determined in a variety of ways including using the 'Elements' inspector tool in
the Google Chrome Developer Console or the 'DOM Inspector' tool in the Firefox Developer Console.
Alternatively, one can open a Python command window, load the desired HTML page, and then parse and exaimine the page contents using BeautifulSoup.
Use of BeautifulSoup's 'prettify()' method can be very helpful to render the reverse-engineered HTML in an nicely indented/formatted 
human-friendly way. (The HTML generated by a webserver is subject to no requirement to deliver nicely-formatted HTML. Quite a few, in fact, 
can and do deliver pages as a single - very long - string.)

Documentation on the BeautifulSoup package can be found [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#).
