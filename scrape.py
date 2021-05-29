import requests
import pandas as pd
from requests_html import HTML 
import datetime 
url = 'https://www.boxofficemojo.com/year/world/2021/'
# to check if the page is responsive
r = requests.get(url)
r.status_code

def url_to_file(url, filename='world.html'):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(filename, 'w') as f:
            f.write(html_text)
        return html_text
    return ""


def parse_data(url, filename='world.html'):
    html_file = url_to_file(url)
    if html_file == None:
        return False

    r_html = HTML(html=html_file)
    table_class = ".imdb-scroll-table"
    status = r_html.find(table_class)

    header_names = []
    table_data = []
    if len(status) == 1:
        parsed_data = status[0]
        rows = parsed_data.find('tr')
        header_rows = rows[0]
        header_cols = header_rows.find('th')
        header_names = [x.text for x in header_cols]

        
        for row in rows[1:]:
            cols = row.find('td')
            row_data = []

            for index, col in enumerate(cols):
                row_data.append(col.text)
            table_data.append(row_data)
            
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv('twenty_twenty_one_movie.csv2', index=False)

parse_data(url)