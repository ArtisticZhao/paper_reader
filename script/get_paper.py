# coding:utf-8
import requests
from lxml import html


def open_url(url):
    print('accessing ' + url + ' ...')
    req = requests.get(url)
    if req.status_code == 200:
        req.encoding = 'GBK'
        return req.text
    else:
        return None


# 得到最近的报纸列表
def get_index(url):
    page = open_url(url)
    tree = html.fromstring(page)
    links = tree.xpath('//div[@class="img-wrap"]/a')
    links_dict = dict()
    for each in links:
        links_dict[each.attrib['title']] = each.attrib['href']
    return links_dict


# 因为页面很规律直接获得全部版面图片地址
def get_day_pic(url):
    index = url.rfind('.')
    pages_link = list()
    for i in range(1, 100):
        if i == 1:
            p_url = url
        else:
            p_url = url[0:index] + '-' + str(i) + '.html'
        page = open_url(p_url)
        if page is None:
            break
        tree = html.fromstring(page)
        link = tree.xpath('//img[@id="demo"]')
        for each in link:
            pages_link.append(each.attrib['src'])

    return pages_link


def get_ckxx_paperlist():
    return get_index('http://www.jdqu.com/bklist-10.html')


if __name__ == '__main__':
    # lks = get_index('http://www.jdqu.com/bklist-10.html')
    # print(lks)
    HOST = 'http://www.jdqu.com'
    lks = get_day_pic(HOST + '/html/ckxx/2019/2/3/1274015.html')
    print(lks)
