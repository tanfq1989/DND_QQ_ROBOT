from filter import msg_route

@msg_route(r'\.help')
def random_attribute(content):
    result=''
    with open('help', 'r+', newline='', encoding='utf-8') as f:
        line = f.readline()
        result=line
        while line:
            line = f.readline()
            result+=line
    return result