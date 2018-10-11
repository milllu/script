#爬取盗版网站的小说,仅用于练习爬虫,不做商业用途,支持正版
import requests
import re
import time
import random

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',}

#获取html信息
def get_html(url):
    req = requests.get(url, headers=header)
    html = req.content.decode('utf-8')
    return html

#获得所有章节url链接
def novel_url_list(url):
    html = get_html(url)
    novel_url = re.findall('<dd>\s*?<a href="(.*?)"', html)
    return novel_url

#单个章节写入文件
def section_content(url, filename):
    html = get_html(url)
    #章节名和内容
    section_name = re.search('<div class="bookname">\s*?<h1>(.*?)</h1>', html)
    section_content = re.search('<div id="content">(.*?)</div>', html)
    name = section_name.groups()[0] 
    content = section_content.groups()[0]
    content = re.sub('&nbsp;', ' ', content)
    content = re.sub('<br />', '\n', content)
    #写入txt文件 
    filename.write(section_name.groups()[0].encode('utf-8'))
    filename.write('\n\n'.encode('utf-8'))
    filename.write(content.encode('utf-8'))
    filename.write('\n\n'.encode('utf-8'))
    print('(已完成)-%s' % name)
    time.sleep(random.randint(1, 3))

def main(url):
    html = get_html(url)
    #提取书名
    file_name_html = re.search('<div id="info">\s*?<h1>(.*?)</h1>', html)
    filename = file_name_html.groups()[0]
    filename = '%s.txt' % filename
    #创建小说文件
    f = open(filename, 'wb')
    novel_list = novel_url_list(url)
    for section_url in novel_list:
        section_url = url + section_url.split('/')[-1]
        section_content(section_url, f)
    f.close()  

if __name__ == '__main__':
    # url = 'https://www.xxbiquge.com/18_18719/'
    url = 'https://www.xxbiquge.com/82_82061/'
    main(url)

    