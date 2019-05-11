from os import makedirs
from os.path import exists
from re import search
from bs4 import BeautifulSoup
import cmfunc

# Made by Zyyans


def get_one_page(soup):

    characters = {}
    nodes = soup.find('div', {'class': 'container'}).find_all('a')

    for node in nodes:
        name = str(search('<a.*?>(.*?)\s<', str(node)).group(1))
        number = str(search('t">.*?[(](.*?)[)].*?<', str(node)).group(1))
        characters[name] = number

    return characters


def get_characters(letters):

    returns = {}
    origin = 'https://zh.nyahentai.com/characters/'
    print('\n正在获取角色列表')

    for letter in letters:

        characters = {}
        count = 0
        nexturl = origin + letter

        while True:

            count = count + 1
            print(' - 正在获取第 ' + str(count) + ' 页名称首字母为 ' + letter + ' 的角色')

            try:

                soup = BeautifulSoup(cmfunc.get_response(nexturl).text, 'lxml')
                characters.update(get_one_page(soup))
                nexturl = soup.find('a', {'rel': 'next'})

                if nexturl:
                    nexturl = nexturl.attrs['href']
                else:
                    break

            except:

                print(' - 连接失败')
                pass

        print('首字母为 ' + letter + ' 的角色列表获取完毕, 正在打印\n请到根目录查看列表\n')

        if not exists(letter + '/'):
            makedirs(letter + '/')

        with open(letter + '/list.txt', 'w') as file:
            for name, number in characters.items():
                file.write(name + ' - 资源数: ' + str(number) + '\n')

        returns.update(characters)

    return returns


def save_book(letter, name, url):

    path = letter + '/' + name + '/'
    if not exists(path):
        makedirs(path)

    soup = BeautifulSoup(cmfunc.get_response(
        url + 'list/1/#pagination-page-top').text, 'lxml')

    for iterator in range(1, int(soup.find('span', {'class': 'num-pages'}).string) + 1):

        print(' - 正在获取第 ' + str(iterator) + ' 张')

        try:

            eachurl = url + 'list/' + str(iterator) + '/#pagination-page-top'
            soup = BeautifulSoup(cmfunc.get_response(eachurl).text, 'lxml')
            pictureurl = soup.find(
                'div', {'class': 'container'}).img.attrs['src']

            with open(path + str(iterator) + '.jpg', 'wb') as file:
                file.write(cmfunc.get_response(pictureurl).content)

        except:

            print(' - 超时')


def get_one_character(character, chinese):

    origin = 'https://zh.nyahentai.com'

    url = origin + '/character/' + \
        character.replace('. ', '-').replace(' ', '-')
    if chinese:
        url = url + '/chinese'

    response = cmfunc.get_response(url)

    if response.ok:

        soup = BeautifulSoup(response.text, 'lxml')
        books = soup.find_all('div', {'class': 'gallery'})

        for book in books:
            name = book.div.string
            link = book.a.attrs['href']
            print('\n - ' + name + ' 获取中')
            save_book(character[0], name, origin + link)

        print('\n该角色资源获取完成\n')

    elif chinese and response.status_code == 404:

        print('该角色不存在中文资源!')
        return

    else:

        print('获取异常!')
        return
