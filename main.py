from bs4 import BeautifulSoup
from os import makedirs
from os.path import exists
from requests import get
from time import sleep


def get_page(url):

    while True:

        try:
            page = get(url, headers={'Connection': 'close'})
            return page
        except:
            sleep(3)

def get_soup(url):
    
    return BeautifulSoup(get_page(url).text, 'lxml')
    
def make_dir(path):
    
    if exists(path) == False:
        makedirs(path)

main_url = get_soup('https://nyahentai.github.io').h2.text
cha_main_url = main_url + '/characters'
cha_links = {}
cha_needs = input('\nWhat are you need? ')
make_dir('lists/')
print('')

for letter in cha_needs:

    print(letter, end=' ')
    cha_url = cha_main_url + '/' + letter
    cha_list = []

    while True:

        cha_soup = get_soup(cha_url)
        cha_divs = cha_soup.find('div', {'class': 'container'}).find_all('a')

        for cha_div in cha_divs:

            cha_links[cha_div.text.split(' (')[0]] = cha_div.attrs['href']
            cha_list.append(cha_div.text)

        print('.', end='')
        if (cha_soup.find('a', {'rel': 'next'}) == None):
            break
        cha_url = main_url + cha_soup.find('a', {'rel': 'next'}).attrs['href']

    with open('lists/' + letter + '.txt', 'w', encoding='utf-8') as txt:
        txt.write('\n'.join(cha_list))
    print('')

make_dir('books/')

while True:

    cha_name = input('\nWhat is his/her name? ')
    cha_chinese = input('Only chinese? (yes/no) ')
    cha_path = 'books/' + cha_name + '/'
    make_dir(cha_path)
    cha_url = main_url + cha_links[cha_name]
    if cha_chinese == 'yes':
        cha_url += '/chinese'
    
    while True:

        cha_soup = get_soup(cha_url)
        bok_divs = cha_soup.find_all('a', {'style': 'padding:0 0 142% 0'})

        for bok_div in bok_divs:

            cha_soup = get_soup(cha_url)
            bok_divs = cha_soup.find_all('a', {'style': 'padding:0 0 142% 0'})

            bok_name = bok_div.find('img', {'is': 'lazyload-image'}).attrs['alt']
            bok_path = cha_path + bok_name.replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('<', '').replace('>', '').replace('|', '') + '/'
            make_dir(bok_path)
            bok_soup = get_soup(main_url + bok_div.attrs['href'])
            pic_divs = bok_soup.find_all('a', {'class': 'gallerythumb'})
            print('\n' + bok_name, end=' ')

            for pic_div in pic_divs:

                pic_url = pic_div.attrs['href']
                pic_soup = get_soup(main_url + pic_url)
                pic_number = str(pic_soup.find('span', {'class': 'current'}).text)
                pic_content = pic_soup.find('img', {'class': 'current-img fit-horizontal'}).attrs['src']
                with open(bok_path + pic_number + '.jpg', 'wb') as jpg:
                    jpg.write(get_page(pic_content).content)
                print('.', end='')

        if (cha_soup.find('a', {'rel': 'next'}) == None):
            print('')
            break
        cha_url = main_url + cha_soup.find('a', {'rel': 'next'}).attrs['href']
