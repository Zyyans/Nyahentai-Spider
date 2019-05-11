import cmfunc
import m1func

print('>> 欢迎使用本子爬虫!')
print('>> 作者: 蠢驴')

while True:

    mode = input('\n>> 已有获取模式如下:\n - 1.按角色名获取\n>> 请选择获取模式: ')
    
    if mode == '1':
    
        print('\n<< 已确认获取模式为: 按角色名获取')
        print('<< 角色获取模块开始运行\n')

        print('>> 请输入您想要获取资源的角色的名称首字母')
        print('>> 每行任意个字母, 按回车确认输入此行内容')
        print('>> 输入 "all" 获取包含所有角色的列表')
        print('>> 输入 "loc" 尝试从本地获取角色列表')
        print('>> 输入 "end" 结束输入\n')
    
        letters = ''
        characters = {}
    
        while True:
    
            key = input()
    
            if key == 'all':
                letters = 'abcdefghijklmnopqrstuvwxyz'
                print('\n<< 已添加所有字母\n')
    
            elif key == 'loc':
                temp = m1func.pull_from_local()
                if type(temp) == dict:
                    characters.update(temp)
                    print('\n<< 已从本地获取角色列表\n')
                else:
                    print('\n<< 未在本地检测到角色列表\n')
    
            elif key == 'end':
                if letters:
                    characters = m1func.get_characters("".join(set(letters)))
                break
    
            else:
                letters = letters + key
    
        print('\n<< 角色列表处理完成')
        print('<< 资源获取模块开始运行\n')

        print('>> 输入格式如下:')
        print('>> 第一行: 您想要获取资源的角色名(角色名请在角色列表中获取)')
        print('>> 第二行: 您是否只需要中文资源(yes/no)')
        print('>> 按回车确认输入此行内容')
        print('>> 输入样例:\n\nhonoka\nyes\n')
        print('>> 样例解释: 获取角色 "honoka" 的所有中文资源')
        print('>> 输入 "all" 获取列表中所有角色的资源')
        print('>> 输入 "end" 结束输入\n')

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

input('>> 程序运行结束, 祝您食用愉快')
