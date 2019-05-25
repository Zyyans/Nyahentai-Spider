from class_Page import Page


class Character(Page):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.url = self.mainurl + 'character/' + name + '/'
        self.list = {}
    
    # 有点累. 先鸽了.
