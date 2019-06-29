from os.path import exists
from re import search

from bs4 import BeautifulSoup

from class_Page import Page


class List(Page):

    def __init__(self, letter):
        super().__init__()
        self.letter = letter
        self.path = 'nyahentai/list/' + letter + '.txt'
        self.list = {}

    def network_init(self):
        self.url = self.mainurl + 'characters/' + self.letter + '/'
        self.soup = self.soup_init(self.url)
        if self.soup:
            print('\n[Info] 首字母为 ' + self.letter + ' 的角色列表初始化完毕\n')
        else:
            print('\n[Info] 首字母为 ' + self.letter + ' 的角色列表初始化失败\n')

    def main(self):
        if self.pull_from_local():
            print('\n[Info] 已从本地获取首字母为 ' + self.letter + ' 的角色列表\n')
        else:
            print('\n[Info] 未在本地找到首字母为 ' + self.letter + ' 的角色列表\n')
        ques = '>> 是否联网获取首字母为 ' + self.letter + ' 的角色列表(yes/no)? '
        ans = input(ques)
        while True:
            if ans == 'yes':
                self.network_init()
                if self.get_characters_list():
                    print('\n[Info] 角色列表获取完毕')
                else:
                    print('\n[Info] 获取角色列表时出现异常')
                if self.push_to_local():
                    print('[Info] 角色列表已保存到本地')
                    print('[Info] 路径为: 软件目录/' + self.path + '\n')
                else:
                    print('[Info] 保存角色列表时出现异常\n')
                break
            elif ans == 'no':
                print('\n[Info] 已跳过联网获取操作\n')
                break
            else:
                ans = input('>> 指令不存在, 请重新输入(yes/no): ')

    def get_characters_list(self):
        if not self.soup:
            return False
        key = 'data-ci-pagination-page'
        number = int(self.soup.find('span', {'class': 'last'}).a.attrs[key])
        for iterator in range(1, number + 1):
            print('>> 正在获取第 ' + str(iterator) + ' 页列表')
            soup = self.soup_init(self.url + 'page/' + str(iterator) + '/')
            tags = soup.find('div', {'class': 'container'}).find_all('a')
            for tag in tags:
                text = tag.text
                name = text.split(' (')[0]
                number = search('[(](.*?)[)]', text).group(1)
                self.list[name] = number
        return True

    def push_to_local(self):
        if self.soup:
            with open(self.path, 'w', encoding='utf-8') as text:
                for name, number in self.list.items():
                    text.write('角色名: ' + name + ' 资源数: ' + number + '\n')
            return True
        else:
            return False

    def pull_from_local(self):
        if exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as text:
                lines = text.readlines()
            for line in lines:
                temp = line.split(' 资源数: ')
                self.list[temp[0].split(': ')[1]] = temp[1]
            return True
        else:
            return False
