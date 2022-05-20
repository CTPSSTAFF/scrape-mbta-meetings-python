#!/usr/bin/env python
# coding: utf-8
# Scrape the MBTA meetings website using Python's BeautifulSoup package

# Import required pacages
import urllib3
from bs4 import BeautifulSoup
import csv

# URL for MBTA meetings page
page_url = "https://www.mbta.com/about/event-list?preview=&vid=latest&nid=5847"

# Create a urllib3 PoolManager instance in order to make HTTP requests. 
# This object handles all of the details of connection pooling and thread safety so that we don't have to.
http = urllib3.PoolManager()

# Read the MBTA meetings web page
response = http.request('GET',page_url)

# Turn the returned HTML into an in-memory data structure that we can query/crawl.
soup = BeautifulSoup(response.data, 'html.parser')

# Take a look at the data structre, pretty-printed
print(soup.prettify())

# Wow! That's a lot of stuff.

# By empirical examination, we know that the 'record' for each meeting
# is 'wrapped' in an HTML <div> element with CSS class 'u-linked-card.
# Find all 'records' in the HTML that meet these search criteria.
# NOTE: Because 'class' is a Python reserved word, the CSS class parameter
#       to our 'find_all' query is specified by the 'class_' parameter (note trailing '_').
#
meetings = soup.find_all('div', class_='u-linked-card')

# Check that the length of the list of results looks 'sane'
len(meetings)

# Get the details about each meeting:
# 1. The title of the meeting is found in the <h3> element within its containing <div>
# 2. The date/time for the meeting is found in the <div> element within the containing <div>
#    with CSS class 'c-content-teaser__date'
# 3. The location of the meeting is found in the <div> element within the containing <div>
#    with CSS class 'c-content-teaser__location'
# 4. The (server-relative) URL for the meeting's webpage is found in the 'href' property
#    of the <a> tag with CSS class 'u-linked-card__primary-link' within the containing <div>
for meeting in meetings:
    title = meeting.find('h3').contents
    date = meeting.find('div', class_="c-content-teaser__date").contents
    location = meeting.find('div', class_="c-content-teaser__location").contents
    anchor = meeting.find('a', class_="u-linked-card__primary-link")
    meeting_url = anchor.get('href')
    # Eyeball sanity check
    print(title)
    print(date)
    print(location)
    print(meeting_url)
#

# List in which we'll accumulate stuff to write out to CSV
output_data = []

# Looks pretty good.
# But there are two things we need to tidy-up:
# 1. Let's clean up any leading and trailing white-space (including '\n') in those strings,
#    and save the whole kit-and-kaboodle in a list of dicts.
# 2. The URL for each meeting's webpage is relative to the root of the MBTA server,
#    so we'll need to prepend 'http://www.mbta.com'/ in order to get a usable URL
for meeting in meetings:
    tmp = meeting.find('h3').contents
    title = tmp[0].strip()
    tmp = meeting.find('div', class_="c-content-teaser__date").contents
    date = tmp[0].strip()
    tmp = meeting.find('div', class_="c-content-teaser__location").contents
    location = tmp[0].strip()
    anchor = meeting.find('a', class_="u-linked-card__primary-link")
    meeting_url = 'http://www.mbta.com/' + anchor.get('href')
    # Eyeball sanity check
    print(title)
    print(date)
    print(location)
    print(meeting_url)
    record = { 'title' : title, 'date' : date, 'location' : location, 'url' : meeting_url }
    output_data.append(record)
#

# Consistency check: number of output records == number of meetings in HTML. Yay!
len(output_data)

# Output the list of dicts as a CSV file.
output_fn = r'C:/Users/ben_k/work_stuff/mbta_meetings.csv'
with open(output_fn, 'w', newline='') as csvfile:
    fieldnames = ['title', 'date', 'location', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in output_data:
        writer.writerow({'title': record['title'], 'date': record['date'], 'location' : record['location'], 'url' : record['url']})
    #
#

# And congratulate ourselves on a job well done.
print("That was easy-peasy. Let's get ice cream!")
