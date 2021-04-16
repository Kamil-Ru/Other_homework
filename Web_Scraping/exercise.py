# TASK: Import any libraries you think you'll need to scrape a website.

import requests
import bs4

# TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.

result = requests.get('http://quotes.toscrape.com/')
print(result.text)

# TASK: Get the names of all the authors on the first page.

soup = bs4.BeautifulSoup(result.text,"lxml")
soup.select('.author')
authors_import = soup.select('.author')
authors = []
for item in authors_import:
    authors.append(item.text)
    
set(authors)
print(*authors, sep = "\n")

#TASK: Create a list of all the quotes on the first page.
text = soup.select(".text")
quotes = []
for items in text:
    quotes.append(items.text)
print(*quotes, sep = "\n")

#TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). 
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.

tag = soup.select(".tag-item")
for item in tag:
    print(item.text)
    
'''TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. 
Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop is on the last page with quotes. 
For debugging purposes, I will let you know that there are only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, 
but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, 
perhaps use try/except for this, its up to you!    '''

base_url = 'http://quotes.toscrape.com/page/{}/'

authors = []
for n in range(1,10):
    res = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(res.text,"lxml")
    authors_import = soup.select('.author')
    for item in authors_import:
        authors.append(item.text)
    
print(set(authors))

# 2
'''
base_url = 'http://quotes.toscrape.com/page/{}/'

authors = []
n = 1
while True:
    try:
        res = requests.get(base_url.format(n))
        soup = bs4.BeautifulSoup(res.text,"lxml")
        authors_import = soup.select('.author')
        for item in authors_import:
            authors.append(item.text)
        n += 1
    if:
        break
set(authors)
'''