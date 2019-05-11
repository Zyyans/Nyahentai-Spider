import cmfunc
import m1func

# Made by Zyyans
print('[蠢驴制造]欢迎使用本子爬虫!\n')

while True:

    mode = input('获取模式如下:\n\n - 1.按角色获取\n\n选择获取模式: ')

    if mode == '1':

        print('\n[蠢驴制造]已确认模式为: 按角色获取')
        print('\n请输入您想要获得资源的角色的名称首字母, 每行任意个字母\n输入"all"以获得包含所有角色的列表, 输入"end"以结束输入\n')

        letters = ''
        while True:
            letter = input()
            if letter == 'all':
                letters = 'abcdefghijklmnopqrstuvwxyz'
                break
            elif letter == 'end':
                break
            else:
                letters = letters + letter

        characters = m1func.get_characters("".join(set(letters)))

        print('请输入您想要获得资源的角色的名称(在列表中选择)\n以及是否只获取中文资源(yes/no)')
        print('输入"all"以获得所有列表中角色的资源, 输入"end"以结束输入\n')
        print('示例输入:\n\na2\nyes\nall\nno\n')
        print('即获取角色"a2"的中文资源和所有角色的所有资源\n')

        while True:

            name = input()
            chinese = input()

            if chinese == 'yes':
                chinese = True
            elif chinese == 'no':
                chinese = False
            elif chinese == 'end':
                break
            else:
                print('\n状态码错误! 请重新输入\n')
                continue

            if name == 'all':
                print('\n请求已接受, 正在处理')
                for name in characters.keys():
                    print(name)
                    m1func.get_one_character(name, chinese)
                break
            elif name == 'end':
                break
            else:
                if name in characters.keys():
                    print('\n请求已接受, 正在处理')
                    m1func.get_one_character(name, chinese)
                else:
                    print('\n该角色不存在于列表中! 请重新输入\n')

        break

    else:
        print('\n模式代码错误! 请重新输入\n')

input('程序运行结束, 祝您食用愉快')
