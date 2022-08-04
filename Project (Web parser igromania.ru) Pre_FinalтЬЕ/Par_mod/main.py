from parse_page import parse
import save_to_csv
import analyzing_data
import plotting_module
from pprint import pprint


# Checking input
url = input('Enter the web page url: ')
url = url.strip()
Flag = True
try:
    url.index('igromania.ru')
    url.index('www.')
    url.index('https://')

    if url.find('hard') == -1 and url.find('news') == -1 and url.find('articles') == -1 \
            and url.find('kino') == -1 and url.find('videos') == -1:
        Flag = False
except ValueError:
    print('Error!')
    Flag = False

# Start code
if Flag:
    num_pages = int(input('Enter number of pages for parsing: '))

    WebPage_info = parse(url, num_pages)
    print(WebPage_info)

    save_to_csv.save_file(WebPage_info, 'Files/igromania_data.csv', 'w')
    print('Done')
