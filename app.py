#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup, Comment

def represents_int(s):
    s = str(s.contents[0])
    try: 
        int(s)
        return True
    except ValueError:
        return False

def get_week_num(s):
    s = str(s.contents[0])
    return int(s)

def main():
    # setup bs4 from url contents
    #url = input('url: ')
    url = 'http://jayurbain.com/msoe/cs3851/outline.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # find the table that we should parse
    # bs4 is dumb otherwise this could be one method
    table = soup.find('table')
    inner_table = table.find('table')
    inner_table_body = inner_table.find('tbody')
    if inner_table is not None:
        table = inner_table_body

    # what to store each week of content in
    weeks = []
    rows = table.find_all('tr')

    # remove the first index containing the column keys
    del rows[0]

    # remove brs
    for e in soup.findAll('br'):
        e.extract()

    for row in rows:
        # determine if this is a new week
        first_cell = row.find('td')
        if represents_int(first_cell):
            week_num = get_week_num(first_cell)
            cells = row.find_all('td')
            del cells[0]
            week_content = []
            for items in cells:
                week_content.append(items)
            weeks.append(week_content)
    print(weeks)

        # weeks
        # [thing one, thing two, thing three]
        # link objects? some sort of custom object?

if __name__ == '__main__':
    main()