from bs4 import BeautifulSoup
from requests import get


class Page():

    def soup_init(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) App\
        leWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        response = get(url, headers=headers)
        if response.ok:
            return BeautifulSoup(response.text, 'lxml')
        else:
            return None


class List(Page):

    def __init__(self, letter):
        super().__init__()
        self.letter = letter
        self.url = 'https://zh.nyahentai.net/characters/' + letter + '/'
        self.soup = self.soup_init(self.url)
        self.path = 'nyahentai/list/' + letter + '.txt'
        self.print_message()

    def print_message(self):
        if self.soup:
            print('\n[Info] 首字母为 ' + self.letter + ' 的角色列表初始化完毕\n')
        else:
            print('\n[Info] 首字母为 ' + self.letter + ' 的角色列表初始化失败\n')

    def main(self):
        if self.get_characters_list():
            print('\n[Info] 角色列表获取完毕')
        else:
            print('\n[Info] 获取角色列表时出现异常')
        if self.push_to_local():
            print('[Info] 角色列表已保存到本地\n')
        else:
            print('[Info] 保存角色列表时出现异常\n')

    def get_characters_list(self):
        if not self.soup:
            return None
        key = 'data-ci-pagination-page'
        number = int(self.soup.find('span', {'class': 'last'}).a.attrs[key])
        self.list = []
        for iterator in range(1, number + 1):
            soup = self.soup_init(self.url + 'page/' + str(iterator) + '/')
            part_list = soup.find('div', {'class': 'container'}).find_all('a')
            self.list.extend(part_list)
            print('>> 正在获取第 ' + str(iterator) + ' 页列表')
        return True

    def push_to_local(self):
        if not self.soup:
            return None
        with open(self.path, 'w', encoding='utf-8') as text:
            for iterator in range(0, len(self.list)):
                text.write(self.list[iterator].text + '\n')
        return True

    # def pull_from_local(self):


print('asd')
List('a').main()
