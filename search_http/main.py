import re

def search_http(filename):
    with open(filename, 'r') as f:
        newl = re.findall('href="(.*)"', f.read())
    return newl
    
def write_to_file(queue):
    with open('https.txt', 'w') as f:
        for i in queue:
            if i and i[-1] == '/':
                i = i[:-1]
            f.write(i + '\n')
    
            
def main():
    queue = search_http('web_page_source_code.txt')
    write_to_file(queue)
    print('http已写入https.txt')

if __name__ == '__main__':
    main()
    
