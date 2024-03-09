import hashlib
import json
import requests
import threading
import random
import queue
import re

ok_url_queue = queue.Queue()

def usera(args):
    headers = {}
    if args.useragent != None:
        headers['User-Agent'] = args.useragent
    elif args.useragent == None:
        user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        ]
        # 随机选择一个
        user_agent = random.choice(user_agent_list)
        headers['User-Agent']=user_agent
    if args.cookie != None:
        headers['cookie'] = args.cookie
    return headers

def finger_scan(args):
    with open(args.file, 'r', encoding='utf-8') as file:
        cms_fg = json.load(file)
    add_protocol_if_needed(args.url, cms_fg , args)
    threads = []
    for _ in range(int(args.theard)):
        thread = threading.Thread(target=process_url, args=(ok_url_queue, cms_fg, args))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def add_protocol_if_needed(url, cms_fg, args):
    for i in range(len(cms_fg)):
        url_with_index = (url + cms_fg[i][0], i)
        ok_url_queue.put(url_with_index)


def process_url(queue, cms_fg, args):
    while not queue.empty():
        url_with_index, current_index = queue.get()
        try:
            url = url_with_index
            index = current_index
            scan_url(url, cms_fg, index, args)
        except:
            pass
        queue.task_done()

def scan_url(url, cms_fg, index,args):
    try:
        porxy = {}
        if args.porxy != None:
            porxy['http'] = f'socks5://{args.porxy}'
            porxy['https'] = f'socks5://{args.porxy}'
        headers = usera(args)
        response = requests.get(url,headers=headers, timeout=3,proxies=porxy)
        if response.status_code == 200:
            content = response.text
            md5_hash = hashlib.md5()
            md5_hash.update(content.encode('utf-8'))
            md5_value = md5_hash.hexdigest()
            if md5_value == str(cms_fg[index][2]):
                print(f'[+] -- {url}\tCMS: {cms_fg[index][1]}')
    except:
        pass
