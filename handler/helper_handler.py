from filter import msg_route
'''
获取帮助信息
'''
@msg_route(r'(\.|。)help')
def random_attribute(content):
    result=''
    with open('help', 'r+', newline='', encoding='utf-8') as f:
        line = f.readline()
        result=line
        while line:
            line = f.readline()
            result+=line
    return result

@msg_route(r'(\.|。)tags$')
def group_pixiv_search(content):
    result = ''
    with open('tags', 'r+', newline='', encoding='utf-8') as f:
        line = f.readline()
        result = line
        while line:
            line = f.readline()
            result += line
    return result