from class_Page import Page


class Character(Page):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.url = self.mainurl + 'character/' + name + '/'
        self.path = 'nyahentai/' + self.name + '/'
        self.list = {}

    def network_init(self, chinese=False):
        if chinese:
            self.url = self.url + 'chinese/'
        self.soup = self.soup_init(self.url)
        if self.soup:
            print('\n[Info] 角色 ' + self.name + ' 的资源列表初始化完毕\n')
        else:
            if chinese == True:
                print('>> 该角色无中文资源')
            print('\n[Info] 角色 ' + self.name + ' 的资源列表初始化失败\n')

# 迟迟没有进展 对其他需要的方法没啥思路 先鸽了
