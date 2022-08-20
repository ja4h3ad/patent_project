from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.parse
from urllib.error import HTTPError
import csv



try:

    url = 'https://patents.google.com/patent/US11045271B1/en'

    print (url)
    req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    print ('Success', url)

except HTTPError as e:
    print('Patent search, Error Status Code : {0}'.format(e))

try:
    inventor = [ x.get_text() for x in soup.find_all('dd', itemprop='inventor')]

except:
    inventor =[]
try:
    pub_date = soup.find('td',itemprop='publicationDate').get_text()
except:
    pub_date = ''
    # Get abstract #
abstract = soup.find('meta', attrs={'name': 'DC.description'})
    # Get text
if abstract:
    abstract_text = abstract['content']

header = ['URL', 'Inventor', 'Publication Date', 'Abstract']
data = [url, inventor, pub_date, abstract_text]


with open('Google_Patents_Scraper.csv', 'w', newline='', encoding = 'UTF8') as f:
    writer= csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)




