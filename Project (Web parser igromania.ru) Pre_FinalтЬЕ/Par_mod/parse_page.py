import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from pprint import pprint

# constant to get access to web page
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
           'accept': '*/*'
           }
# path to chrome driver
PATH = '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages' \
       '/selenium/webdriver/chrome/chromedriver'


# Getting access to web page
# url - link of the web page
# Returns response code
def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


# Getting information from web page
# html - code of web page
def get_content(html):
    # Getting html code, filling list with article data
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='aubl_item')

    # Filling data: title, subtitle, author, section, date
    data = []
    for item in items:
        author = item.find('div', class_='aubli_data').find('div', class_='aubli_date').find('span')
        # Checking if author name is exist on the tab
        if author is not None:
            author = author.get_text(strip=True).replace('|\xa0', '')
        try:
            data.append({
                'title': item.find('div', class_='aubli_data').find('a', class_='aubli_name').get_text(strip=True),
                'subtitle': item.find('div', class_='aubli_data').find('div', class_='aubli_desc').get_text(strip=True),
                'date': item.find('div', class_='aubli_data').find('div', class_='aubli_date').get_text()[:10],
                'author': author,
                'section': item.find('div', class_='aubli_data').find('div', class_='aubli_sect').get_text(strip=True)
            })
        except AttributeError:
            pass

    return data


# Extending page by adding new articles (click button on web page)
# url - link of the web page
# pages_num - number of pages for parsing
def extend_page(url, pages_num):
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')

    # Open virtual browser
    driver = webdriver.Chrome(executable_path=PATH, options=opt)
    driver.get(url)

    # Getting access to more articles
    for i in range(pages_num-1):
        element = driver.find_element_by_class_name('lcol').find_element_by_class_name('aubl_smore')
        element.click()
        time.sleep(1)

    # Getting html code of the page
    driver.find_element_by_tag_name('html')
    page_code = driver.page_source
    driver.quit()

    return page_code


# Parsing web page
def parse(url, num_pages):
    try:
        html = get_html(url)
        if num_pages == 1:
            html_code = html.text
        else:
            html_code = extend_page(url, num_pages)
    except Exception:
        html_code = html.text
    if html.status_code == 200:
        article_info = get_content(html_code)
        return article_info
    else:
        print('Error! Try another link')
        return None
